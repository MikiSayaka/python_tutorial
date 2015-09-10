from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#  Basic database decleration
engine = create_engine("postgresql+psycopg2://amtdev:admin@139.162.4.179/mom_noodles", echo=True)

Base = declarative_base()


#  Mapping configuration and mapping object
class Account(Base):
    __tablename__ = "account"

    user_id = Column(Integer, primary_key = True)
    email = Column(String(100))

    def __repr__(self):
        return "<User(email='%s')>" % (self.email)

#  Create schema
Account.__table__

Base.metadata.create_all(engine)


#  Create instance
account_inst = Account(email = "a8965128@gmail.com")

print account_inst.email


#  Session create
Session = sessionmaker(bind=engine)

Session.configure(bind = engine)

session = Session()
