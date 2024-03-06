#!/usr/bin/python3
"""City Class module"""
from models.base_model import BaseModel
"""imports BaseMOdel module"""


class City(BaseModel):
    """ City class

    Attributes:
        state_id: it will be the State.id
        name: name of City
    """

    state_id = ""
    name = ""
