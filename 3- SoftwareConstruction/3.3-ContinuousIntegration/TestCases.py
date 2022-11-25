from unittest import TestCase
from main import Courses


class TestCourses(TestCase):
    def setUp(self):
        self.courses = Courses("null")

    def test_create_lesson_with_Введення_у_СУБД_11_11_2022_08_00(self):
        self.assertTrue(self.courses.create_lesson('Введення у СУБД', '11.11.2022', '08:00'))

    def test_create_lesson_with_error_Введення_у_СУБД_11_11_2022_08_mi(self):
        with self.assertRaises(ValueError, msg="Результат = -1"):
            self.courses.create_lesson('Введення у СУБД', '11.11.2022', '08:mi')

    def test_create_lesson_with_error_Введення_у_СУБД_ккк_1111_2022_08_00(self):
        with self.assertRaises(ValueError, msg="Результат = -2"):
            self.courses.create_lesson('Введення у СУБД','ккк.1111.2022', '08:00')

    def test_create_lesson_with_error_Введення_у_СУБД___1111_2022_08_00(self):
        with self.assertRaises(ValueError, msg="Результат = -3"):
            self.courses.create_lesson('', '11.11.2022', '08:00')
