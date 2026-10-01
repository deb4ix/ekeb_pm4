import unittest
from ekeb_service import print_cost, exam_result, Student

# Задание 1
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

# Задание 2
class TestExamResult(unittest.TestCase):

    def test_minus_one(self):
        with self.assertRaises(ValueError):
            exam_result(-1)

    def test_zero(self):
        self.assertEqual(exam_result(0), "Незачёт")

    def test_forty_nine(self):
        self.assertEqual(exam_result(49), "Незачёт")

    def test_fifty(self):
        self.assertEqual(exam_result(50), "Зачёт")

    def test_fifty_one(self):
        self.assertEqual(exam_result(51), "Зачёт")

    def test_hundred(self):
        self.assertEqual(exam_result(100), "Зачёт")

    def test_one_hundred_one(self):
        with self.assertRaises(ValueError):
            exam_result(101)

# Задание 3
class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("Алия", 50)

    def test_name(self):
        self.assertEqual(self.student.name, "Алия")

    def test_initial_score(self):
        self.assertEqual(self.student.score, 50)

    def test_boundary_score(self):
        self.assertTrue(self.student.has_passed())

    def test_add_points(self):
        self.assertEqual(self.student.add_points(10), 60)

    def test_max_score(self):
        self.assertEqual(self.student.add_points(60), 100)

    def test_negative_points(self):
        with self.assertRaises(ValueError):
            self.student.add_points(-10)

if __name__ == "__main__":
    unittest.main()