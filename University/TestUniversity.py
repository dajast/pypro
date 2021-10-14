import unittest
from University.Student import Student
from University.Course import Course
from University.Curriculum import Curriculum


class TestUniversity(unittest.TestCase):
    def setUp(self):  # called before every testmethod
        self.student = Student('Martin Tester')
        self.course = Course('TestCourse')
        self.curriculum = Curriculum()

    def test_1(self):
        self.student.enroll('Mathe')
        self.assertIn('Mathe', self.curriculum.get_course_titles(), msg='Mathe not contained in {}'.format(self.curriculum))

    def test_2(self):
        self.student.enroll('Mathe', 'Bio', 'Science')
        self.assertIn('Mathe', self.curriculum.get_course_titles(), msg='Mathe not contained in {}'.format(self.curriculum))
        self.assertIn('Bio', self.curriculum.get_course_titles(), msg='Bio not contained in {}'.format(self.curriculum))
        self.assertIn('Science', self.curriculum.get_course_titles(), msg='Science not contained in {}'.format(self.curriculum))

    def test_3(self):
        self.course.add_participant(self.student)
        self.assertIn('Martin Tester', map(lambda student: student._name, self.course.get_course_participants()))


if __name__ == '__main__':
    unittest.main()
