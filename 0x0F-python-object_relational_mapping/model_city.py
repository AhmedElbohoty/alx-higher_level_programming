#!/usr/bin/python3
''' City Model '''
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sys
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base


class City(Base):
    '''City model'''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'))
