from University.Course import Course


class Curriculum:
    course: Course
    courses = set()
    course_titles = set()

    def __init__(self):
        pass

    def add_course_to_curriculum(course: Course):
         if course.course_title not in Curriculum.course_titles:
             Curriculum.course_titles.add(course.course_title)
             Curriculum.courses.add(course)
         else:
             pass

    @classmethod
    def get_courses(cls):
        print(str(cls.courses))
        return cls.courses

    @classmethod
    def get_course(cls, course_title):
        # returns the course-obj of a course-title
        # print(str(cls.courses))
        for course in cls.courses:
            try:
                if course.course_title == course_title:
                    return course
            except Exception:
                print('No course ', course_title, ' found!')

    @classmethod
    def get_course_titles(cls) -> []:
        # for title in Curriculum.course_titles:
        #     print('Titles in Course-Titles ', title)
        return cls.course_titles


