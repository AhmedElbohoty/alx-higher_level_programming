#!/usr/bin/python3
''' City Model '''
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class City(Base):
    '''City model'''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'))
