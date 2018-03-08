import unittest

from faker import Faker

from example import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        self.user = User(
            first_name = self.fake.first_name(),
            last_name = self.fake.last_name(),
            job = self.fake.job(),
            address = self.fake.address()
        )

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)

    def test_user_name(self):
        expected_username = self.user.first_name + " " + self.user.last_name
        self.assertEqual(expected_username, self.user.user_name)
