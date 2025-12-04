from sqlalchemy import Column,Integer,String
from database import base

class Client(base):
    __tablename__="Clients"
    __table_args__={"schema":"public"}


    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)



