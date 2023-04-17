import os
import logging
from dotenv import load_dotenv
from passlib.context import CryptContext


load_dotenv()
environment = os.environ["ENVIRONMENT"]
database_name = os.environ["DATABASE_NAME"]


def setup_db(
    environment: str = environment,
    database_name: str = database_name
):
    # Deleting DB if in local or test environment
    if environment in ['local', 'test']:
        if os.path.exists(database_name):
            os.remove(database_name)
            logging.warning(f'Removed database: {database_name}')


    # Importing the db client
    from powerdict.db import get_db_client
    db_client = get_db_client()


    ## Adding development DB records
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


if __name__ == "__main__":
    setup_db()
