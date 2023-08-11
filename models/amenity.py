#!/usr/bin/python3
'''class of BaseModel'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''amenity class'''

    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity initializing"""
        super().__init__(*args, **kwargs)
