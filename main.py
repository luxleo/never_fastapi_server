from typing import Union
from fastapi import FastAPI

from pydantic import BaseModel
from model import LyricTagDao,SongDao
from service import LyricTagService,SongService
from view import create_endpoints
from sqlalchemy import create_engine

from config import settings

class People(BaseModel):
    name:str
    age:int
    hoppy: Union[str,None]
class Services:
    pass
def create_app(test_config=None):
    app = FastAPI()
    if test_config is None:
        db_config = settings.DB_URL
    else:
        db_config = settings.test_config["DB_URL"]
    database = create_engine(db_config, encoding='utf-8',max_overflow=0)
    song_dao = SongDao(database)
    lyric_tag_dao = LyricTagDao(database)
    services = Services
    services.song_service = SongService(song_dao)
    services.lyric_tag_service = LyricTagService(lyric_tag_dao)

    create_endpoints(app,services)
    return app
app = create_app()
