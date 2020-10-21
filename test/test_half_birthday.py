import unittest
import date_time
import datetime


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(date_time.half_birthday(), datetime.datetime(2004, 3, 17, 0, 0))


if __name__ == '__main__':
    unittest.main()
