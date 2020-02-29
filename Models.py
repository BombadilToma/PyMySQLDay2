from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base#fuggveny ami classet terit vissza
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True,autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))

    def __str__(self):
        return f"<Student #{self.id} {self.first_name} {self.last_name}>"

class Locker(Base):
    __tablename__ = "lockers"
    number = Column(Integer, primary_key= True)
    student = Column(Integer, ForeignKey(Student.id), primary_key = True)

    def __str__(self):
        return f"<Locker {self.number}: {self.student}>"

class Address(Base):
    __tablename__ = "Address"
    student = Column(Integer, ForeignKey(Student.id), primary_key = True)
    street_name = Column(String(255))
    number = Column(Integer)
    city = Column(String(255))

    def __str__(self):
        return f"<Students Address: {self.street_name}, {self.number}>"

class Grades(Base):
    __tablename__ = "Grades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student = Column(Integer, ForeignKey(Student.id))
    grade = Column(Integer)
    date_created = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"<Student {id} has the following grade: {grade}>"