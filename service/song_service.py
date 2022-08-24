class SongService:
    def __init__(self,song_dao):
        self.song_dao = song_dao

    def create_new_song(self,new_song):
        new_song_id = self.song_dao.insert_song(new_song)
        return new_song_id

    def song_list(self,query):
        res= self.song_dao.get_song_list(query)
        if not res :
            res = [{
                "title":"dummy",
                "artist":"dummy",
                "e_label":2,
                "v_label": 3,
                "mood_tag": "test_tag",
                "id": 1
            }]
            return res
        return res

    def song_list_with_mood_tag(self,query):
        res= self.song_dao.get_song_list_with_mood_tag(query)
        if res ==[]:
            res = [{
                "title":"dummy",
                "artist":"dummy",
                "e_label":2,
                "v_label": 3,
                "mood_tag": f"{query}",
                "id": 1
            }]
            return res
        return res

    def mood_tags(self):
        res = self.song_dao.get_mood_tags()
        if res == []:
            res = [{"tag":"슬픈"},{"tag":"잔잔한"},{"tag":"역동적인"}]
            return res
        return res