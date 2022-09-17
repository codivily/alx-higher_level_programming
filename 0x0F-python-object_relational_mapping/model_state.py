#!/usr/bin/python3
""" This module contain a State class """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ A class that represent a State """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
