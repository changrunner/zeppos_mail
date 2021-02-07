import unittest
from zeppos_mail.email import Email


class TestTheProjectMethods(unittest.TestCase):
    def test_send_methods(self):
        self.assertEqual(True, Email().send())


if __name__ == '__main__':
    unittest.main()
