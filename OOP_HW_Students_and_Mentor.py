class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # def add_courses(self, course_name):
    # #     self.finished_courses.append(course_name)

    # Выставление оценок за лекции лекторам. Заполняется словарь self.grades_lect = {} у лекторов
    def rate_lecture(self, lectuter, course, grade):
        if isinstance(lectuter, Lectuter) and course in lectuter.courses_attached and course in self.courses_in_progress or course in self.finished_courses:
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

    def __lt__(self, student):
        if not isinstance(student, Student):
            print(f'Нет такого студента')
            return
        return self.average_grade() < student.average_grade()


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

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lectuter):
            print(f'Нет такого лектора')
            return
        return self.average_grade_lecture() < lecturer.average_grade_lecture()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress or course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f"Имя: {self.name}\nФамилия: {self.surname}"
        return some_reviewer

def average_grades_students_hw(students_list, course):
    student_rating = 0
    lectors = 0
    for stud in students_list:
        if course in stud.grades.keys():
            average_student_grade = 0
            for grades in stud.grades[course]:
                average_student_grade += grades
            student_rating = average_student_grade / len(stud.grades[course])
            average_student_grade += student_rating
            lectors += 1
    if student_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{student_rating / lectors:.2f}'

def average_grades_lecturers(lecturer_list, course):
    average_rating = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.grades_lect.keys():
            lecturer_average_rates = 0
            for rate in lecturer.grades_lect[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.grades_lect[course])
            average_rating += overall_lecturer_average_rates
            b += 1
    if average_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{average_rating / b:.2f}'


student_1 = Student('Вася', 'Пупкин', 'муж')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses = ['Introduction']

student_2 = Student('Оля', 'Петрова', 'жен')
student_2.courses_in_progress = ['Python', 'Git']
student_2.finished_courses = ['Introduction']
students_list = [student_1, student_2]


lecturer_1 = Lectuter('Олег', 'Булыгин')
lecturer_1.courses_attached = ['Python']

lecturer_2 = Lectuter('Евгений', 'Шмаргунов')
lecturer_2.courses_attached = ['Introduction', 'Git']
lecturer_list = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Александр', 'Бардин')
reviewer_1.courses_attached = ['Python']
reviewer_2 = Reviewer('Олег', 'Булыгин')
reviewer_2.courses_attached = ['Introduction', 'Git']

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 9)

reviewer_2.rate_hw(student_1, 'Introduction', 10)
reviewer_2.rate_hw(student_2, 'Introduction', 6)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 9)


student_1.rate_lecture(lecturer_1, 'Python', 8)
student_1.rate_lecture(lecturer_2, 'Git', 9)
student_1.rate_lecture(lecturer_2, 'Introduction', 10)
student_2.rate_lecture(lecturer_1, 'Python', 10)
student_2.rate_lecture(lecturer_2, 'Git', 8)
student_2.rate_lecture(lecturer_2, 'Introduction', 8)




print(student_1)
print(student_2)
print(f'Средняя оценка студентов по курсу "Introduction": {average_grades_students_hw(students_list, "Introduction")}')
print(f'Средняя оценка студентов по курсу "Git": {average_grades_students_hw(students_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Python": {average_grades_students_hw(students_list, "Python")}')
if student_1 > student_2:
    print(f'{student_1.name} учится лучше, чем {student_2.name}')
else:
    print(f'{student_2.name} учится лучше, чем {student_1.name}')

print(lecturer_1)
print(lecturer_2)
print(f'Средняя оценка лектора по курсу "Introduction": {average_grades_lecturers(lecturer_list, "Introduction")}')
print(f'Средняя оценка лектора по курсу "Git": {average_grades_lecturers(lecturer_list, "Git")}')
print(f'Средняя оценка лектора по курсу "Python": {average_grades_lecturers(lecturer_list, "Python")}')
if lecturer_1 > lecturer_2:
    print(f'{lecturer_1.name} {lecturer_1.surname} преподает лучше, чем {lecturer_2.name} {lecturer_2.surname}')
else:
    print(f'{lecturer_2.name} {lecturer_2.surname} преподает лучше, чем {lecturer_1.name} {lecturer_1.surname}')

print(reviewer_1)
print(reviewer_2)



