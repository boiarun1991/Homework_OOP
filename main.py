class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []

    grades = {}

    def give_rate_mentor(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in Lecturer.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mid_grades(self):
        list_grades = [list_grades for all_grades in Student.grades.values() for list_grades in all_grades]
        avarage_grade = sum(list_grades) / len(list_grades)
        return avarage_grade

    def __str__(self):
        return (
            f'''Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {Student.mid_grades(self)}
Курсы в процессе обучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}''')

    def __lt__(self, other):
        return self.mid_grades() < other.mid_grades()

    def __gt__(self, other):
        return self.mid_grades() > other.mid_grades()

    def __eq__(self, other):
        return self.mid_grades() == other.mid_grades()

    def __ne__(self, other):
        return self.mid_grades() != other.mid_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def mid_grades(self):
        list_grades = [list_grades for all_grades in Lecturer.grades.values() for list_grades in all_grades]
        avarage_grade = sum(list_grades) / len(list_grades)
        return avarage_grade

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {Lecturer.mid_grades(self)}'

    def __lt__(self, other):
        return self.mid_grades() < other.mid_grades()

    def __gt__(self, other):
        return self.mid_grades() > other.mid_grades()

    def __eq__(self, other):
        return self.mid_grades() == other.mid_grades()

    def __ne__(self, other):
        return self.mid_grades() != other.mid_grades()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Oksana', 'Naugolnykh', 'female')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']

student_2 = Student('Rob', 'Stark', 'male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']

reviewer_1 = Reviewer('Alex', 'Popov')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Anna', 'Larkova')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

lecturer_1 = Lecturer('Viktoria', 'Bondugina')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Kris', 'Nikulina')
lecturer_2.courses_attached += ['Git']

# Выставление оценок студентам курсов Python и Git:
reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Git', 6)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Git', 3)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Git', 5)
reviewer_2.rate_hw(student_2, 'Python', 4)
reviewer_2.rate_hw(student_2, 'Git', 8)

# Выставление оценок лекторам курсов Python и Git:
student_1.give_rate_mentor(lecturer_1, 'Python', 10)
student_1.give_rate_mentor(lecturer_1, 'Git', 10)
student_1.give_rate_mentor(lecturer_2, 'Python', 6)
student_1.give_rate_mentor(lecturer_2, 'Git', 8)

student_2.give_rate_mentor(lecturer_2, 'Python', 10)
student_2.give_rate_mentor(lecturer_2, 'Git', 9)
student_2.give_rate_mentor(lecturer_1, 'Python', 6)
student_2.give_rate_mentor(lecturer_1, 'Git', 9)

some_reviewer = reviewer_2

some_lecturer = lecturer_1

some_student = student_2
some_student.finished_courses += ['Введение в программирование', 'Английский для IT']

print(some_reviewer, '\n')
print(some_lecturer, '\n')
print(some_student, '\n')

students = [student_1, student_2]
lectors = [lecturer_1, lecturer_2]


# Возможность сравнения лекторов и студентов по средней оценке:
print(lecturer_1 > student_1)
print(lecturer_1 == student_2)
print(lecturer_2 < student_1)
print(lecturer_2 != student_2)

def mid_rating_students(students, course):
    return sum(Student.grades.get('Python')) / len(students)


def mid_rating_lectors(lecturers, course):
    return sum(Lecturer.grades.get('Git')) / len(lectors)


print(mid_rating_students(students, 'Git'))
print(mid_rating_lectors(lectors, 'Python'))


