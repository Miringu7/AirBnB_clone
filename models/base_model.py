#!/usr/bin/python3
"""Base Class module"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
    """Initialization of Base class model"""
    self.id = str(uuid.uuid4()
    self.created_at = datetime.now()
    self.updated_at = daetime.now()

    def __str__(self):
        """Returns representation of Base Model"""
        return "[{}], ({}), {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()

     def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        dictt = self.__dict__.copy()
        dictt['__class__'] = self.__class__.__name__
        dictt['created_at'] = self.created_at.isoformat()
        dictt['updated_at'] = self.updated_at.isoformat()
        return dictt
