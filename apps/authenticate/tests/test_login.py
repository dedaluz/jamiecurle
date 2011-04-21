from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from apps.users.models import UserProfile


class LoginCases(TestCase):
    
    def setUp(self):
        u = User()
        u.set_password('test')
        u.email = 'test@example.com'
        u.save()
        self.u = u
    
    
    def test_can_login_with_username(self):
        """ensure we can login with username """
        #
        r = self.client.post(reverse('authenticate:login'), {'username': 'test@example.com', 'password' : 'test'})
        # get the user again
        self.assertEqual(302, r.status_code)
