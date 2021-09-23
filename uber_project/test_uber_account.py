import unittest
import uber_account


class MyTestCase(unittest.TestCase):
    def test_uber_account(self):
        day_toll = round(toll.sum(), 2)

        self.assertEqual(day_toll, 85.35)  # add assertion here


if __name__ == '__main__':
    unittest.main()
