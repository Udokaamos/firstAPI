# # import email
from django.test import TestCase
from .models import Song

# # Create your tests here.


class SongTestcase(TestCase):

    # @classmethod
    def text_song(self):
        Song.objects.create('title', 'artist', 'publish_date', 'date_created')

#     def test_song(self):
#         song= Song.objects.get(id=1)
#         # print(hashed_password)

        self.assertEqual(str(Song), "title")
        self.assertEqual(Song.artist, "")
        self.assertEqual(Song.publish_date, "John")
        self.assertEqual(Song.date_created)

    def test_all_song(self):
        songs = Song.objects.all()
        self.assertEqual(songs.count(), 0)