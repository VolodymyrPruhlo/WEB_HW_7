from faker import Faker
from connect import session
from models import Grade, Groups, Students, Teachers, Classes
import random


if __name__ == "__main__":
    faker = Faker()

    for _ in range(3):
        group = Groups(group_name=faker.word())
        session.add(group)
    session.commit()

    # Створення викладачів
    for _ in range(3):
        teacher = Teachers(
            name=faker.first_name(), surname=faker.last_name(), email=faker.email()
        )
        session.add(teacher)
    session.commit()

    # Створення предметів (класів) і призначення викладачів
    teachers = session.query(Teachers).all()
    for _ in range(5):
        teacher = random.choice(teachers)
        class_ = Classes(classes_name=faker.word(), teacher=teacher)
        session.add(class_)
    session.commit()

    # Створення студентів
    groups = session.query(Groups).all()
    for _ in range(30):
        group = random.choice(groups)
        student = Students(
            name=faker.first_name(),
            surname=faker.last_name(),
            email=faker.email(),
            group=group,
        )
        session.add(student)
    session.commit()

    # Створення оцінок
    students = session.query(Students).all()
    classes = session.query(Classes).all()
    for student in students:
        for class_ in classes:
            for _ in range(
                random.randint(5, 20)
            ):  # Генерація від 5 до 20 оцінок для кожного студента з кожного предмету
                grade = Grade(
                    value=random.randint(1, 5), student=student, subject=class_
                )
                session.add(grade)
    session.commit()

    print("Database has been seeded.")
