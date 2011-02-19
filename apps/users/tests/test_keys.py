from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from apps.users.models import UserProfile


class KeyTestCases(TestCase):
    
    def test_key_remains_the_same(self):
        # set up a user
        u = User()
        u.username = 'test'
        u.set_password('test')
        u.email = 'test@example.com'
        u.save()
        # store the key
        pre_login_key = u.get_profile().key
        # now login as the user
        r = self.client.post(reverse('authenticate:login'), {'username': u.username, 'password' : 'test'})
        # get the user again
        post_login_key = User.objects.get(pk=u.pk).get_profile().key
        #
        self.assertEqual(pre_login_key, post_login_key)


