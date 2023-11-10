class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # Выставление оценок за лекции лекторам. Заполняется словарь self.grades_lect = {} у лекторов
    def rate_lecture(self, lectuter, course, grade):
        if isinstance(lectuter, Lectuter) and course in lectuter.courses_attached and course in self.courses_in_progress:
            if isinstance(grade, int) and (0 <= grade <= 10):
                if course in lectuter.grades_lect:
                    lectuter.grades_lect[course] += [grade]
                else:
                    lectuter.grades_lect[course] = [grade]
            else:
                print('Неправильно введена оценка')
        else:
            return 'Ошибка'

    # Расчет средней арифм оценки за домашние задания
    def average_grade(self):
        total = 0
        count = 0
        for grade in self.grades.values():
            count += len(grade)
            for item in grade:
                total += item
        return round(total / count, 1)

    def __str__(self):
        some_student = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание:{self.average_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lectuter(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lect = {}

# Расчет средней арифм оценки за лекции
    def average_grade_lecture(self):
        total = 0
        count = 0
        for grade in self.grades_lect.values():
            count += len(grade)
            for item in grade:
                total += item
        return round(total / count, 1)


    def __str__(self):
        some_lecturer = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade_lecture()}"
        return some_lecturer

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f"Имя: {self.name}\nФамилия: {self.surname}"
        return some_reviewer


some_student = Student('Вася', 'Пупкин', 'муж')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses = ['Введение в програмирование']


some_lecturer = Lectuter('Олег', 'Булыгин')
some_lecturer.courses_attached += ['Python', 'Git']

some_reviewer = Reviewer('Александр', 'Бардин')
some_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

some_student.rate_lecture(some_lecturer, 'Python', 8)
some_student.rate_lecture(some_lecturer, 'Git', 9)
some_student.rate_lecture(some_lecturer, 'Введение в програмирование', 10)

print(some_student.grades)
print(some_student.grades)
print(some_lecturer.grades_lect)

print(some_reviewer)
print(some_lecturer)
print(some_student)