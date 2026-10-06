import unittest

from course_service import Course


class TestCourse(unittest.TestCase):

    def test_create_course(self):
        course = Course("Python", 20)

        self.assertEqual(course.name, "Python")
        self.assertEqual(course.capacity, 20)

    def test_new_course_has_zero_enrolled(self):
        course = Course("Python", 20)

        self.assertEqual(course.enrolled, 0)

    def test_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            Course("", 20)

    def test_zero_capacity_raises_error(self):
        with self.assertRaises(ValueError):
            Course("Python", 0)

    def test_negative_capacity_raises_error(self):
        with self.assertRaises(ValueError):
            Course("Python", -5)

    def test_available_places(self):
        course = Course("Python", 20)

        self.assertEqual(course.available_places(), 20)

if __name__ == "__main__":
    unittest.main()