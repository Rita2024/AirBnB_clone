#!/usr/bin/python3
'''class BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''city of class'''

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """City initialization"""
        super().__init__(*args, **kwargs)
