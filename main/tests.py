# # import email
from django.test import TestCase
from django.utils import timezone
from .models import Song

# # Create your tests here.
date = timezone.now()

class SongTestcase(TestCase):
    

    @classmethod
    def setUpTestData(cls):
        Song.objects.create(title="Assurance", artist="Davido", publish_date=date)

    def test_Song(self):
        song= Song.objects.get(id=1)
        # print(hashed_password)

        # self.assertEqual(str(song), "Assurance")
        self.assertEqual(song.title, "Assurance")
        self.assertEqual(song.artist, "Davido")
        self.assertEqual(song.publish_date, date)

    def test_all_song(self):
        songs = Song.objects.all()
        self.assertEqual(songs.count(), 1)