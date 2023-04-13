from powerdict import db

db_fp = 'tests/data/dictionary.db'

db_client = db.DbClient(
    database_name=db_fp,
    dialect='sqlite',
    driver=None,
)
