# Завдання 1
# Створіть клас Message з атрибутами
#  user – ім’я автора повідомлення
#  text – текст повідомлення
#  time – час повідомлення(використайте модуль datetime)
# приклад datetime.strptime('10:23', '%H:%M')
# методи:
#  __str__(self) – повертає текст повідомлення та час
#  __len__(self) – повертає довжину повідомлення
#  __gt__(self, other) – перевіряє чи є повідомлення self
# старішим за other
# Створіть список з декількома повідомленнями та виведіть
# його. Відсортуйте список і знову виведіть
import datetime
from typing import List


# class Message:
#
#     def __init__(self, user: str, text: str, time:str):
#         self._user = user
#         self._text = text
#         self._time = datetime.datetime.strptime(time, '%H:%M')
#
#     def __str__(self):
#         return f"user {self._user}, message {self._text}, time {self._time.time()}"
#
#     def __len__(self):
#         return len(self._text)
#
#     def __gt__(self, other):
#         return self._time > other._time
#
#
#
# message = Message("Alina", "hello", "14:35")
# print(message)
# print(len(message))
# message_other = Message("New user", "new user", "15:35")
# print(message>message_other)
#
# messages= []
# messages.append(Message("Dan", "Message1", "12:56"))
# messages.append(Message("Anna", "Message2", "13:56"))
# messages.append(Message("John", "Message3", "07:35"))
#
# for message in messages:
#     print(message)
#
# messages.sort()
# for message in messages:
#     print(message)

# Завдання 2
# Створіть клас Song з атрибутами
#  name – назва пісні
#  author – ім’я автора
# Практичне завдання
# методи:
#  __eq__(self, other) – перевіряє чи дві пісні однакові
#  __str__(self, other) – повертає рядок з назвою та автором

# Створіть клас Playlist з атрибутами
#  songs – список пісень(об’єкти класу Song)
# методи:
#  __len__(self) – повертає кількість пісень
#  __contains__(self, item) – перевіряє чи є пісня в плейлисті
#  __iter__(self) – повертає літератор для циклу for
#  add_song(self, song) – додає пісню в плейлист
#  remove_song(self, song) – видаляє пісню з плейлиста
# Створіть порожній плейлист
# Створіть 3 пісні:
# "Imagine", "John Lennon"
# "Bohemian Rhapsody", "Queen"
# "Shape of You", "Ed Sheeran"
# Добавте їх в плейлист
# Пройдіться циклом for по плейлисту та виведіть кожну
# пісню на екран

class Song:

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __eq__(self, other):
        if isinstance(other, Song):
            return self._name == other._name and self._author == other._author

        else:
            return False


    def __str__(self):
        return f"Song: name {self._name}, author {self._author}"

song_1 = Song("Shape of You", "Ed Sheeran")
song_2 = Song("Blinding Lights", "The Weeknd")
song_3 = Song("Imagine", "John Lennon")

print(song_1)
print(song_1 == song_2)

class Playlist:

    def __init__(self):
        self.songs: List[Song] = []

    def __len__(self):
        return len(self.songs)

    def __contains__(self, item):
        return item in self.songs

    def __iter__(self):
        return iter(self.songs)

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
        else:
            "Song is already in the list"

    def remove_song(self, song):
        if song in self.songs:
            self.songs.pop(song)
        else:
            "Song is not in the list"
