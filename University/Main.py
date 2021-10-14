from University.Student import Student
from University.Curriculum import Curriculum


def start():
    # del Curriculum
    s1 = Student('Maik')
    s1.enroll('Math', 'Art', 'Art', 'Math', 'Computer Science', 'Economics')
    s1.get_details()

    s2 = Student('Janine Schmidt')
    s2.enroll('Psychology', 'Medicine', 'Yoga', 'Sport', 'Construction', 'Yoga', 'Math', 'Art')
    s2.get_details()

    s3 = Student('Holger IV')
    s3.enroll('Science', 'Economics', 'Math')
    s3.get_details()

    print('Curriculum: ', [title for title in Curriculum.course_titles])
    subj = 'Math'
    print('Participants:', subj,
          str([student._name for student in Curriculum.get_course(subj).get_course_participants()]))
    subj = 'Yoga'
    print('Participants:', subj,
          str([student._name for student in Curriculum.get_course(subj).get_course_participants()]))
    subj = 'Economics'
    print('Participants:', subj,
          str([student._name for student in Curriculum.get_course(subj).get_course_participants()]))
    subj = 'Art'
    print('Participants:', subj,
          str([student._name for student in Curriculum.get_course(subj).get_course_participants()]))

    # c = Curriculum()
    # s = Student('Max')
    # s.enroll('Biology', 'Geophysics')
    # s.get_details()
    # print('Curriculum: ', [titles for titles in c.course_titles], c.course_titles)



class StartUniversity():
    if __name__ == '__main__':
        start()
