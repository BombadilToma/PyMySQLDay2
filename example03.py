from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from Secrets import user, host, password
from Models import Student

CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{db}"
eng = create_engine(
    CONNECTION_STRING.format(
        user= user, password=password, host=host, db="default"
                             )
)

Session = sessionmaker(bind = eng)
s = Session()

rows = s.query(Student).all()
for row in rows:
    print(row)

print("-------")
total = s.query(Student).count()
print (f"Total = {total}")

print("-------")
query_result = s.query(Student).filter(Student.id>=2, Student.first_name.like("Jim%"))
print("Found students:")


for row in query_result:
    print(row)

print("------")
ion = s.query(Student).filter(Student.first_name=="Nucky").first()

#Set new last name
ion.last_name = 'Enoch'

#Commit the chan
s.commit()

query_result = s.query(Student).filter(Student.last_name.like("Eno%"))
for row in query_result:
    print(row)