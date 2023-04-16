import os
from copy import deepcopy
from dotenv import load_dotenv
from typing import Optional
from datetime import datetime, timedelta
from sqlalchemy.exc import NoResultFound
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from powerdict import schemas, db

db_client = db.get_db_client()


# Inputs
load_dotenv()

JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
JWT_ALGORITHM = os.environ["JWT_ALGORITHM"]
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"])
REFRESH_WARNING_MINUTES = int(os.environ["REFRESH_WARNING_MINUTES"])


# OAuth and DB setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="authentication/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

CredentialsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


# Auth helper functions
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = deepcopy(data)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise CredentialsException
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise CredentialsException
    user = get_user(username=token_data.username)
    if user is None:
        raise CredentialsException
    return user


def get_current_active_user(
    current_user: schemas.SecureAPIUser = Depends(get_current_user),
) -> schemas.SecureAPIUser:
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user.")
    return current_user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_current_active_superuser(
    current_user: schemas.SecureAPIUser = Depends(get_current_user),
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user.")
    if not current_user.is_superuser:
        raise HTTPException(status_code=400, detail="Not a superuser.")
    return current_user


def get_user(username: str) -> Optional[schemas.SecureAPIUser]:
    try:
        return db_client.get_record(username, 'api__secure_user')
    except NoResultFound:
        return None


def authenticate_user(user, password) -> bool:
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False

    return True


def create_user(
    username: str,
    name: str,
    email: str,
    password: str,
    is_superuser: bool = False
):
    try:
        db_client.get_record(username, 'api__secure_user')
        raise ValueError(f'Username already exists: {username}')
    except NoResultFound:
        pass

    hashed_password = get_password_hash(password)

    user = db.SecureAPIUserTable(
        username=username,
        name=name,
        email=email,
        hashed_password=hashed_password,
        disabled=False,
        is_superuser=is_superuser,
    )

    _ = db_client.create_record(user, tablename='api__secure_user')

    return user


# Routes
router = APIRouter(tags=["Authentication"])

@router.post("/token", response_model=schemas.Token, include_in_schema=False)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    authenticated = authenticate_user(user, form_data.password)

    if not authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )

    token_record = db.TokenRecordTable(
        username=user.username,
        token=access_token,
        expires=datetime.utcnow() + access_token_expires,
    )

    _ = db_client.create_record(token_record, tablename='api__tokens')

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me/", response_model=schemas.APIUser, include_in_schema=False)
async def read_users_me(
    current_user: schemas.SecureAPIUser = Depends(get_current_active_user),
):
    return current_user
