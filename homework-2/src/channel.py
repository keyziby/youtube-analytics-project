import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('API_YouTube')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        youtube = self.get_service()
        self.dict_to_print = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        dict_youtube = json.loads(json.dumps(self.dict_to_print, indent=2, ensure_ascii=False))
        self.title = dict_youtube["items"][0]["snippet"]["title"]
        self.description = dict_youtube["items"][0]["snippet"]["description"]
        self.subscriberCount = dict_youtube["items"][0]["statistics"]["subscriberCount"]
        self.video_count = dict_youtube["items"][0]["statistics"]["videoCount"]
        self.viewCount = dict_youtube["items"][0]["statistics"]["viewCount"]
        self.url = dict_youtube["items"][0]["snippet"]["thumbnails"]["default"]["url"]

    def get_service(self):
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        return youtube

    def to_json(self, file_name):
        data = {
            "id": self.__channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscriberCount": self.subscriberCount,
            "video_count": self.video_count,
            "viewCount": self.viewCount
        }
        with open(file_name, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @property
    def channel_id(self):
        return self.__channel_id

    # def print_info(self) -> None:
    #     """Выводит в консоль информацию о канале."""
    #     print(json.dumps(self.dict_to_print, indent=2, ensure_ascii=False))
    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
