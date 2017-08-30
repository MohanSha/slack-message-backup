import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        user = User()
        user.password= "hello"

        self.assertTrue(user.password_hash is not None)

    def test_no_password_getter(self):
        user = User()
        user.password= "hello"
        with self.assertRaises(AttributeError):
            user.password

    def test_password_verification(self):
        user = User()
        user.password= "hello"
        self.assertTrue(user.verify_password("hello"))
        self.assertFalse(user.verify_password("hi"))

    def test_password_random(self):
        user = User()
        user.password= "hello"
        user2 = User()
        user2.password= "hello"
        self.assertTrue(user.password_hash != user2.password_hash)
