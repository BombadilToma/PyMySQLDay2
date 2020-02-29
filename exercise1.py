from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Secrets import host, user, password
from Models import Address, Student, Base


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
        Address(street_name = "Butcher Street", number = 7, city = "Atlantic City", student=1),
        Address(street_name = "Baker Street", number = 22, city = "London", student=2),
        Address(street_name =  "Old Town", number = 42, city = "Los Angeles", student=3)

    ])
except IntegrityError:
    sess.rollback()
    print("already created")

rows = sess.query(Student,Address).join(Address).filter(Address.city.like("L%"))
for row in rows:
    student, address = row
    print(f"Student with address #{student}: {address}")