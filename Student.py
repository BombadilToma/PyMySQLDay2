from sqlalchemy import create_engine
from Models import Base, Student
from Secrets import host, user, password

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"
eng = create_engine(
    CONNECTION_STRING.format(user= user, password=password, host=host, db="default"
                             )
)
Base.metadata.create_all(eng)