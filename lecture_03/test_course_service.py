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


if __name__ == "__main__":
    unittest.main()