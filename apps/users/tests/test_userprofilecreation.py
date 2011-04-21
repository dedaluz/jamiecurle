from django.test import TestCase
from django.contrib.auth.models import User
from apps.users.models import UserProfile

class UserProfileCreationTestCase(TestCase):
    
    def test_creation(self):
        # we have none
        self.assertEqual(0, User.objects.count())
        self.assertEqual(0, UserProfile.objects.count())
        # make one
        u = User()
        u.username = 'test'
        u.set_password('test')
        u.email = 'test@example.com'
        u.save()
        # we have one
        self.assertEqual(1, User.objects.count())
        self.assertEqual(1, UserProfile.objects.count())
        # and it belongs to our user
        profile = UserProfile.objects.get(pk=1)
        self.assertEqual(u.get_profile().pk, profile.pk)