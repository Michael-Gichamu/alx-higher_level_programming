#!/usr/bin/python3
"""
python file that contains class defination of
State and an instance Base = declarative_base()
"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from enum import unique

Base = declarative_base()


class State(Base):
    """
    Class State
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
