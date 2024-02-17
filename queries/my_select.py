from connect import session
from models import Grade, Groups, Students, Classes
from sqlalchemy import func, desc


def select_1():
    return (
        session.query(
            Students.name,
            Students.email,
            func.round(func.avg(Grade.value), 2).label("avg_grade"),
        )
        .select_from(Grade)
        .join(Students)
        .group_by(Students.students_id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )


def select_2(subject_id):
    subquery = (
        session.query(Grade.student_id, func.avg(Grade.value).label("average_score"))
        .filter(Grade.classes_id == subject_id)
        .group_by(Grade.student_id)
        .subquery()
    )
    return (
        session.query(Students.name, subquery.c.average_score)
        .join(Students, Students.students_id == subquery.c.student_id)
        .order_by(subquery.c.average_score.desc())
        .first()
    )


# Знайти середній бал у групах з певного предмета.
def select_3(course_id):
    return (
        session.query(
            Classes.classes_name, func.avg(Grade.value).label("average_score")
        )
        .join(Students, Students.group_id == Classes.classes_id)
        .join(Grade, Grade.student_id == Students.students_id)
        .filter(Grade.classes_id == course_id)
        .group_by(Classes.classes_name)
        .all()
    )


# Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4():
    return session.query(func.avg(Grade.value)).scalar()


# Знайти які курси читає певний викладач.
def select_5(teacher_id):
    return (
        session.query(Groups.group_name).filter(Groups.teacher_id == teacher_id).all()
    )


# Знайти список студентів у певній групі.
def select_6(group_id):
    return session.query(Students.name).filter(Students.group_id == group_id).all()


# Знайти оцінки студентів у окремій групі з певного предмета.
def select_7(group_id, course_id):
    return (
        session.query(Students.name, Grade.value)
        .join(Grade, Grade.student_id == Students.students_id)
        .filter(Students.group_id == group_id, Grade.classes_id == course_id)
        .all()
    )


# Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(teacher_id):
    return (
        session.query(func.avg(Grade.value))
        .join(Classes, Classes.classes_id == Grade.classes_id)
        .filter(Classes.teacher_id == teacher_id)
        .scalar()
    )


# Знайти список курсів, які відвідує певний студент.
def select_9(student_id):
    return (
        session.query(Classes.classes_name)
        .join(Grade, Grade.classes_id == Classes.classes_id)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )


# Список курсів, які певному студенту читає певний викладач.
def select_10(student_id, teacher_id):
    return (
        session.query(Classes.classes_name)
        .join(Grade, Grade.classes_id == Classes.classes_id)
        .filter(Grade.student_id == student_id, Classes.teacher_id == teacher_id)
        .distinct()
        .all()
    )
