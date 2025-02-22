#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from models.review import Review
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table


if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False)
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if storage_type == 'db':
        city_id = Column(
                String(60),
                ForeignKey('cities.id'),
                nullable=False)
        user_id = Column(
                String(60),
                ForeignKey('users.id'),
                nullable=False)
        name = Column(
                String(128),
                nullable=False)
        description = Column(
                String(1024),
                nullable=True)
        number_rooms = Column(
                Integer,
                nullable=False,
                default=0)
        number_bathrooms = Column(
                Integer,
                nullable=False,
                default=0)
        max_guest = Column(
                Integer,
                nullable=False,
                default=0)
        price_by_night = Column(
                Integer,
                nullable=False,
                default=0)
        latitude = Column(
                Float,
                nullable=True)
        longitude = Column(
                Float,
                nullable=True)
    else:
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

        @property
        def reviews(self):
            """returns the list of Review instances with
            place_id equals to the current Place.id"""
            from models import storage
            all_revs = storage.all(Review)
            lst = []
            for rev in all_revs.values():
                if rev.place_id == self.id:
                    lst.append(rev)
            return lst

        @property
        def amenities(self):
            ''' returns the list of Amenity instances
                based on the attribute amenity_ids that
                contains all Amenity.id linked to the Place
            '''
            from models import storage
            all_amens = storage.all(Amenity)
            lst = []
            for amen in all_amens.values():
                if amen.id in self.amenity_ids:
                    lst.append(amen)
            return lst

        @amenities.setter
        def amenities(self, obj):
            ''' method for adding an Amenity.id to the
                attribute amenity_ids. accepts only Amenity
                objects
            '''
            if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
