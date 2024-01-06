import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('api_key')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.current_channel = self.get_service().channels().list(id=self.__channel_id,
                                                                  part='snippet,statistics').execute()
        self.title = self.current_channel["items"][0]["snippet"]["title"]
        self.description = self.current_channel["items"][0]["snippet"]["description"]
        self.subscriberCount = self.current_channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.current_channel["items"][0]["statistics"]["videoCount"]
        self.viewCount = self.current_channel["items"][0]["statistics"]["viewCount"]
        self.url = self.current_channel["items"][0]["snippet"]["customUrl"]

    def get_service(self):
        return build('youtube', 'v3', developerKey=self.api_key)

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


