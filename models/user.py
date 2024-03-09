#!/usr/bin/python3
"""User Class module"""
from models.base_model import BaseModel
"""imports BaseMOdel module"""


class User(BaseModel):
    """ User class

    Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
