from pydantic import BaseModel
from typing import Union

class Song(BaseModel):
    title:str
    artist:str
    e_label:Union[int,None] = None
    v_label:Union[int,None] = None
    mood_tag:Union[str,None] = None

class LyricTag(BaseModel):
    tag_name:str
class SongTagMap(BaseModel):
    song_id:int
    tag_id:int

def create_endpoints(app,services):
    song_service = services.song_service
    lyric_tag_service = services.lyric_tag_service

    #ping test
    @app.get('/ping')
    def ping():
        return "pong"

    ##song 검색창에 검색했을때 query에 맞는 노래 모두 반환
    @app.get('/song/')
    def get_list_of_songs_with_search(q:Union[str,None] = None):
        songs = song_service.song_list(q)
        return {"songs":songs}
    #mood tag 클릭 했을때 해당 곡들 반환
    @app.get('/song/moodtag/{query}')
    def click_mood_tag_and_get_song_list(query:str):
        songs = song_service.song_list_with_mood_tag(query)
        return {
            "songs":songs
        }
    #lyrics tag를 눌렀을때 해당 곡들을 반환
    @app.get('/song/lyrictag/{tag_id}')
    def click_lyrictag_and_get_songs(tag_id:int):
        songs = lyric_tag_service.song_list_of_lyric_tag(tag_id)
        return {
            "songs":songs
        }
    #mood tag들 반환
    @app.get('/moodtag')
    def get_all_mood_tags():
        tags = song_service.mood_tags()
        return {
            "mood_tags":tags
        }

    #song list 클라이언트단에서 각 곡의 가사기반 태그듧 반환
    @app.get('/lyrictag/song/{song_id}')
    def get_lyrictag_of_each_song(song_id:int):
        lyric_tags = lyric_tag_service.lyric_tags_of_song(song_id)
        return {
            "lyric_tags":lyric_tags
        }
    #검색창에 lyric태그 기반으로 검색 했을때 lyric태그 들을 반환
    @app.get('/lyrictag/{query}')
    def get_matching_lyrictags_when_search(query:Union[str,None]=None):
        tags = lyric_tag_service. lyric_tags_with_query(query)
        return {
            "lyric_tags":tags
        }
    @app.post('/create/song')
    def insert_song_into_db(song:Song):
        song = dict(song)
        new_song_id = song_service.create_new_song(song)
        if new_song_id:
            return '',200
        return 'failed', 404

    @app.post('/create/lyrictag')
    def insert_lyrictag_into_db(lyrictag:LyricTag):
        new_tag = dict(lyrictag)
        new_tag_name = new_tag["tag_name"]
        new_tag_id = lyric_tag_service.create_new_lyric_tag(new_tag_name)
        if new_tag_id:
            return '',200
        return 'failed', 404
    @app.post('/create/map')
    def create_map(map:SongTagMap):
        payload = dict(map)
        new_map_tag_id = payload['tag_id']
        new_map_song_id = payload['song_id']
        check = lyric_tag_service.create_new_map(new_map_tag_id,new_map_song_id)
        if check:
            return '',200
        return 'failed',404