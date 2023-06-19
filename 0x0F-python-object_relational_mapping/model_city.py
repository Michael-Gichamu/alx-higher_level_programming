#!/usr/bin/python3
"""
Defines a City model.
Inherits from Sqlalchemy Base and links to the MySql table cities.
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    Represents a city for MySQl database.
    Attributes:
        id (str): The city's id.
        name (sqlalchmey.integer): The city's name.
        state_id (sqlalchemy.String): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship(State)
