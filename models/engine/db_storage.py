#!/usr/bin/python3
"""database storage engine"""
import sqlalchemy
import sqlalchemy.orm
import os
from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage:
    """This i a class for the module db_storage"""
    __engine = None
    __session = None

    def __init__(self):
        """class constructor"""
        self.__engine = sqlalchemy.create_engine(
                "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                os.getenv('HBNB_MYSQL_USER'),
                os.getenv('HBNB_MYSQL_PWD'),
                os.getenv('HBNB_MYSQL_HOST'),
                os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        all objects depending of the class name (argument cls)"""
        objects = {}
        
