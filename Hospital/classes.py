from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    phone_no = Column(Integer)

# Creating the database engine
my_engine = create_engine('sqlite:///hospital.db')
Base.metadata.create_all(my_engine)

# Creating a session to interact with the database
my_session = sessionmaker(bind=my_engine)
active_session = my_session()

# Creating a patient record
Patient1 = Patient(name='Craig', age=25, phone_no='078988765')
active_session.add(Patient1)
active_session.commit()
