import unittest
from models import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('username', 'qwerty')

    def tearDown(self):
        ...

    def test_login(self):
        self.assertEqual(self.user.login, 'username')

    def test_cart(self):
        self.assertEqual(len(self.user.cart), 0)


if __name__ == '__main__':
    unittest.main()
