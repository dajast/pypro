"""Exercise
Write a class Student, with the following methods:
• constructor
• get_details(self)
• enroll(self, course)
• get_no_of_students(self)
• get_course_participants(self, course)
• __str__()
Take care of class vs. Instance variables.
"""

from University.Course import Course
from University.Curriculum import Curriculum

class Student(object):
    """A class Student with constructor, get_details(self), enroll(self, course),
       get_no_of_students(self), get_course_participants(self, course), __str__()
    """

    def __init__(self, name):
        self._name = name
        self._courses_of_student = set()

    def get_details(self):
        print(self.__str__())
        # print(str(self))
        # return self.__str__()

    def enroll(self, *course_title) -> None:
        for title in course_title:
            if title not in Curriculum.course_titles:
                new_course = self.create_course(title)
                if new_course:
                    self._courses_of_student.add(new_course)
            else:
                self._courses_of_student.add(Curriculum.get_course(title))
            Curriculum.get_course(title).add_participant(self)

    def create_course(self, title):
        # from University.Curriculum import Curriculum
        if title not in Curriculum.get_course_titles():
            new_course = Course(title)
            Curriculum.add_course_to_curriculum(new_course)

            return new_course
        else:
            pass #return None #'course already exists'

    def __str__(self):
        return 'Sudentname = ' + str(self._name) + '. Courses: ' + str([el.course_title for el in self._courses_of_student] ) + '\n'

