from  Secrets import host, user, password
from sqlalchemy.orm import sessionmaker
from Models import Base, Grades
from sqlalchemy import create_engine


CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"
eng = create_engine(
    CONNECTION_STRING.format(
        user= user, password=password, host=host, db="default"
                             )
)

Base.metadata.create_all(eng)

Session = sessionmaker(bind = eng)
sess = Session()

try:
    sess.add_all([
        Grades(student=1, grade =3),
        Grades(student=2, grade =6),
        Grades(student=3, grade =9)

    ])
except IntegrityError:
    sess.rollback()
    print("already created")

