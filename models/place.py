#!/usr/bin/python3
"""State Class module"""
from models.base_model import BaseModel
"""imports BaseMOdel module"""


class Place(BaseModel):
    """ State class

    Attributes:
        city_id: it will be the City.id
        user_id: it will be the User.id
        name: name of the place
        description: information about place
        number_rooms: rooms per place
        number_bathrooms: bathrooms per room
        max_guest: maximum number of guests
        price_by_night: amount for a night
        latitude: location
        longitude: location
        amenity_ids: it will be the list of Amenity.id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
