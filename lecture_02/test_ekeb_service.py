import unittest
from ekeb_service import print_cost

class TestPrintCost(unittest.TestCase):

    def test_zero_pages(self):
        self.assertEqual(print_cost(0), 0)

    def test_one_page(self):
        self.assertEqual(print_cost(1), 30)

    def test_nine_pages(self):
        self.assertEqual(print_cost(9), 270)

    def test_ten_pages(self):
        self.assertEqual(print_cost(10), 270)

    def test_eleven_pages(self):
        self.assertEqual(print_cost(11), 297)

    def test_negative_pages(self):
        with self.assertRaises(ValueError):
            print_cost(-1)

if __name__ == "__main__":
    unittest.main()