import os
from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from powerdict.api import frictionless, authentication


# Inputs
load_dotenv()
middleware_secret_key = os.environ["MIDDLEWARE_SECRET_KEY"]
environment = os.environ["ENVIRONMENT"]

# Initialisation
app = FastAPI(
    title="Power Station Dictionary",
    description="Welcome to the Power Station Dictionary API",
    version="0.1.0"
)

app.add_middleware(SessionMiddleware, secret_key=middleware_secret_key)

app.include_router(frictionless.router, prefix="/frictionless")
app.include_router(authentication.router, prefix="/authentication")

if environment in ['local', 'test']:
    if authentication.get_user('ayrton') is None:
        authentication.create_user(
            username = 'ayrton',
            name = 'ayrton',
            email = 'ayrtonbourn@outlook.com',
            password = 'password',
            is_superuser = True
        )
