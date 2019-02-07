import os

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set. Please set it with 'export {}:<your value>'".format(name, name)
        raise Exception(message)

POSTGRES_URL = get_env_variable("DATABASE_URL")
POSTGRES_USER = get_env_variable("DATABASE_USER")
POSTGRES_PW = get_env_variable("DATABASE_PW")
POSTGRES_DB = get_env_variable("DATABASE_DB")

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)