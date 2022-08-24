from pydantic import BaseSettings

class Settings(BaseSettings):
    db:dict = {
    'user': 'root',
    'password':'150303kj!',
    'host':'localhost',
    'port':3306,
    'database':'never'
    }
    DB_URL:str = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
    test_db:dict = {
    'user': 'root',
    'password':'150303kj!',
    'host':'localhost',
    'port':3306,
    'database':'never_test'
    }
    test_config:dict = {"DB_URL": f"mysql+mysqlconnector://{test_db['user']}:{test_db['password']}@{test_db['host']}:{test_db['port']}/{test_db['database']}?charset=utf8"}


settings = Settings()