#!/usr/bin/python3
"""State Class module"""
from models.base_model import BaseModel
"""imports BaseMOdel module"""


class State(BaseModel):
    """ State class

    Attributes:
        place_id: string - it will be the Place.id
        user_id: string - it will be the User.id
        text: review text by user
    """

    place_id = ""
    user_id = ""
    text = ""
