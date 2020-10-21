import unittest
import assign_average


class MyTestCase(unittest.TestCase):
    def test_A(self):
        self.assertEqual("You entered an A!", assign_average.switch_average('A'))

    def test_B(self):
        self.assertEqual("You entered an B!", assign_average.switch_average('B'))

    def test_C(self):
        self.assertEqual("You entered an C!", assign_average.switch_average('C'))


if __name__ == '__main__':
    unittest.main()
