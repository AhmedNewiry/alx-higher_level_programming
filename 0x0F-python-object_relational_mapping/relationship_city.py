#!/usr/bin/python3
""" Contains the class definition of the model City
"""


from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class City(Base):
    """python mapping of cities table"""
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name',String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


