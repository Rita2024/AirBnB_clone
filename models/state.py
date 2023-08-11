#!/usr/bin/python3
'''class BaseModel'''
from models.base_model import BaseModel


class State(BaseModel):
    '''State of class'''

    name = ""

    def __init__(self, *args, **kwargs):
        """initialize the State"""
        super().__init__(*args, **kwargs)
