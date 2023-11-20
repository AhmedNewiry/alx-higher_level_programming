#!/usr/bin/python3
""" Contains the class definition of the model City
"""


from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship

if __name__ == '__main__':
    class City(Base):
        __tablename__ = 'cities'
        id = Column('id', Ineger, primary_key=true, nullable=false)
        name = Column('name',String(128), nullable=false)
        state_id = Column(Integer, nullable=false,ForeignKey('states.id'))
        state = relationship("State", back_populates='cities')


