#!/usr/bin/python3
"""Base Class module"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes:"""
    def __init__(self, *args, **kwargs):
        """Initialization of Base class model

        Arguments:
            args: strings
            kwargs: key value pair
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns representation of Base Model"""
        return "[{}], ({}), {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dict containing all key/value of
            __dict__ of the instance
        """
        dictt = self.__dict__.copy()
        dictt['__class__'] = self.__class__.__name__
        dictt['created_at'] = self.created_at.isoformat()
        dictt['updated_at'] = self.updated_at.isoformat()
        return dictt
