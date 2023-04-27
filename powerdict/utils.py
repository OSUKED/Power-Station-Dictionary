import os
import datetime
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

        # adding test user
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

        # adding example site
        db_records = {
            'dict__register': [
                {
                    'osuked_id': 10221,
                    'date_added': datetime.datetime.now(),
                    'asset_type': 'power_station',
                    'common_name': 'London Array',
                }
            ],
            'dict__link_repd': [
                {
                    'osuked_id': 10221,
                    'repd_id': 2511,
                    'date_added': datetime.datetime.now()
                },
                {
                    'osuked_id': 10221,
                    'repd_id': 2507,
                    'date_added': datetime.datetime.now()
                }
            ],
            'dict__link_bmu': [
                {
                    'osuked_id': 10221,
                    'bmu_id': 'T_LARYW-1',
                    'date_added': datetime.datetime.now()
                },
                {
                    'osuked_id': 10221,
                    'bmu_id': 'T_LARYW-2',
                    'date_added': datetime.datetime.now()
                },
                {
                    'osuked_id': 10221,
                    'bmu_id': 'T_LARYW-3',
                    'date_added': datetime.datetime.now()
                },
                {
                    'osuked_id': 10221,
                    'bmu_id': 'T_LARYW-4',
                    'date_added': datetime.datetime.now()
                }
            ]
        }

        db_client.create_multi_table_records(db_records=db_records)


if __name__ == "__main__":
    setup_db()
