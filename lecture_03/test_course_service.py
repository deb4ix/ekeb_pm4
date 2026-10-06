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

    def test_enroll_one_student(self):
        course = Course("Python", 2)

        remaining = course.enroll()

        self.assertEqual(course.enrolled, 1)
        self.assertEqual(remaining, 1)

    def test_enroll_until_full(self):
        course = Course("Python", 2)

        self.assertEqual(course.enroll(), 1)
        self.assertEqual(course.enroll(), 0)

    def test_enroll_when_full_raises_error(self):
        course = Course("Python", 1)

        course.enroll()

        with self.assertRaises(ValueError):
            course.enroll()

    def test_cancel_enrollment(self):
        course = Course("Python", 2)

        course.enroll()
        course.cancel_enrollment()

        self.assertEqual(course.enrolled, 0)
        self.assertEqual(course.available_places(), 2)

    def test_cancel_when_empty_raises_error(self):
        course = Course("Python", 2)

        with self.assertRaises(ValueError):
            course.cancel_enrollment()

if __name__ == "__main__":
    unittest.main()