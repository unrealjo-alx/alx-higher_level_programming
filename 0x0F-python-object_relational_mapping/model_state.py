#!/usr/bin/python3
"""
model_state.py : a file that contains the class definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Clas State"""

    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(256), nullable=False)
