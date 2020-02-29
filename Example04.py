from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from Models import Base, Student, Locker
from Secrets import user, host, password
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"
eng = create_engine(
    CONNECTION_STRING.format(
        user= user, password=password, host=host, db="default"
                             )
)
Base.metadata.create_all(eng)
Session = sessionmaker(bind = eng)
s = Session()

try:
    s.add_all(
        [
        Locker(number = 1, student = 4),
        Locker(number=2, student=3),
        Locker(number=3, student=2),
        Locker(number=4, student=1)
]
    )
    s.commit()
except IntegrityError:
    s.rollback()
    print("Lockers already created")

rows = s.query(Student,Locker).join(Locker).filter(Locker.number == 4)
for row in rows:
    student, locker = row
    print(f"Student with locker #{locker.number}: {student}")
