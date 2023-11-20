#!/usr/bin/python3
"""
Class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base

class City(Base):
    """
    City class inherits from Base
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(string(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
