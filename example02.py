from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models import Base, Student
from Secrets import user, host, password

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"
eng = create_engine(
    CONNECTION_STRING.format(user= user, password=password, host=host, db="default"
                             )
)

Session = sessionmaker(bind = eng)
s = Session()
s.add_all(
    [
        Student(first_name = "Jimmy", last_name = "Darmody"),
        Student(first_name = "Nucky", last_name = "Thompson"),
        Student(first_name = "Arnold", last_name = "Rothstein")


    ]



)
s.commit()

