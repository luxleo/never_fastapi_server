class LyricTagService:
    def __init__(self,lyric_tag_dao):
        self.dao = lyric_tag_dao


    def create_new_lyric_tag(self,tag_name):
        new_lyric_tag_id = self.dao.insert_lyric_tag(tag_name)
        return new_lyric_tag_id

    def create_new_map(self,tag_id,song_id):
        check = self.dao.insert_map(tag_id,song_id)
        return check

    def song_list_of_lyric_tag(self,lyric_tag_id):
        res = self.dao.get_song_list_of_lyric_tag(lyric_tag_id)
        if res == []:
            res = [{
                "title":"dummy",
                "artist":"dummy",
                "e_label":2,
                "v_label": 3,
                "mood_tag": "test_mood_tag",
                "id": 1
            }]
            return res
        return res

    def lyric_tags_of_song(self,song_id):
        tags = self.dao.get_lyric_tags_of_song(song_id)
        if tags == []:
            tags = [{
                "id":1,"tag":"드라이브"
            },{
                "id":2,"tag":"한강"
            }]
            return tags
        return tags

    def lyric_tags_with_query(self,query):
        res = self.dao.get_lyric_tags_with_query(query)
        if res == []:
            res = [{
                "id":1,"tag":"운동"
            },{"id":2,"tag":"운동광"}]
            return res
        return res
