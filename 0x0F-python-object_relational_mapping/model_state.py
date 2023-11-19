#!/usr/bin/python3
"""a python file that contains the class definition of a State"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """represents states table in the database"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=True)
    cities = relationship("City", back_populates="state", cascade="all, delete, delete-orphan")
