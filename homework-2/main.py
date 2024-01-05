from src.channel import Channel

if __name__ == '__main__':
    mr_bst = Channel('UCX6OQ3DkcsbYNE6H8uQQuVA')

    # получаем значения атрибутов
    print(mr_bst.title)  # MoscowPython
    print(mr_bst.video_count)  # 685 (может уже больше)
    print(mr_bst.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    # менять не можем
    mr_bst.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscowpython.json' в данными по каналу
    mr_bst.to_json('youtube.json')
