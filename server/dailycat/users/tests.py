from django.test import TestCase
from django.db.utils import IntegrityError

from .models import User


class UserModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_user_instance(self):
        user = User.objects.create(email='test@test.com')
        self.assertIsInstance(user, User)

    # unique하게 되는지
    # invalid email 거부
    def test_user_not_created_if_exist(self):
        duplicate_email = 'test@duplicate.com'
        user = User.objects.create(email='test@uplicate.com')
        with self.assertRaises(IntegrityError):
          User.objects.create(email='test@uplicate.com')

    # TODO: 잘못된 email의 경우 생성되지 않아야함
    def test_user_not_created_if_invalid_email(self):
        invalid_email = 'test'
        user = User.objects.create(email='1234')
        self.assertTrue(User.objects.filter(email='1234').exists())