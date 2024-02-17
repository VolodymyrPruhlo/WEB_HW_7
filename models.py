from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped


class Base(DeclarativeBase):
    pass


class Teachers(Base):
    __tablename__ = "teachers"

    teacher_id: Mapped[int] = mapped_column(primary_key=True)
    name = mapped_column(String(30))
    surname = mapped_column(String(30))
    email = mapped_column(String(30))
    lesson = relationship("Classes", back_populates="teacher")
    group = relationship("Groups", back_populates="teacher")


class Groups(Base):
    __tablename__ = "groups"

    group_id: Mapped[int] = mapped_column(primary_key=True)
    group_name = mapped_column(String(30))
    teacher_id: Mapped[int] = mapped_column(ForeignKey(Teachers.teacher_id))
    student = relationship("Students", back_populates="group")
    teacher = relationship("Teachers", back_populates="group")


class Students(Base):
    __tablename__ = "students"

    students_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    surname = mapped_column(String(50))
    email = mapped_column(String(50))
    group_id: Mapped[int] = mapped_column(ForeignKey(Groups.group_id))
    grades = relationship("Grade", back_populates="student")
    group = relationship("Groups", back_populates="student")


class Classes(Base):
    __tablename__ = "classes"

    classes_id: Mapped[int] = mapped_column(primary_key=True)
    classes_name = mapped_column(String(30))
    teacher_id = mapped_column(ForeignKey(Teachers.teacher_id))
    teacher = relationship("Teachers", back_populates="lesson")
    grades = relationship("Grade", back_populates="subject")


class Grade(Base):
    __tablename__ = "grades"

    grade_id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[int]
    datatime_id: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    classes_id: Mapped[int] = mapped_column(ForeignKey(Classes.classes_id))
    student_id: Mapped[int] = mapped_column(ForeignKey(Students.students_id))
    student = relationship("Students", back_populates="grades")
    subject = relationship("Classes", back_populates="grades")
