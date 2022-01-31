# # import email
# from django.test import TestCase


# # from koalaAPI.main.models import Song

# # Create your tests here.


# class SongModelTestcase(TestCase):

#     @classmethod
#     def setUpTestData(cls):
#         User.objects.create(first_name="Peter", last_name="John", password="111b2", email="email@gmail.com", phone="090398475895")

#     def test_single_user(self):
#         user = User.objects.get(id=1)
#         # print(hashed_password)

#         self.assertEqual(str(user), "email@gmail.com")
#         self.assertEqual(user.first_name, "Peter")
#         self.assertEqual(user.last_name, "John")
#         self.assertEqual(check_password('111b2', user.password), True)

#     def test_all_song(self):
#         songs = Song.objects.all()
#         self.assertEqual(songs.count(), 1)