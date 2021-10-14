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
# from University import Student


class Course(object):

    def __init__(self, title):
        self.course_title = title
        self.participants = set()

    def add_participant(self, student):
        self.participants.add(student)
        return self.participants

    def get_course_participants(self):
        return self.participants



    def __str__(self):
        return 'Course-Title = ' + str(self.course_title) + ', Participants: ' + str(self.participants)


