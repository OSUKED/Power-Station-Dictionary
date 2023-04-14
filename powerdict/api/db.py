import logging
import os
from dotenv import load_dotenv
from passlib.context import CryptContext

from powerdict import db


load_dotenv()
environment = os.environ["ENVIRONMENT"]

db_fp = 'tests/data/dictionary.db'

if environment in ['local', 'test']:
    os.remove(db_fp)

db_client = db.DbClient(
    database_name=db_fp,
    dialect='sqlite',
    driver=None,
)

if environment in ['local', 'test']:
    db_client.create_tables()

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    db_client.create_record(
        record = {
            'username': 'tester',
            'name': 'tester',
            'email': 'tester@gmail.com',
            'hashed_password': pwd_context.hash('password'),
            'is_superuser': True

        },
        tablename = 'api__secure_user'
    )
