import sqlite3
# This is a helper class hence its in Model; internal representation of an entity
from db import db

class UserModel(db.Model):

    # below rows help save the class properties to SQLAlchemy, these should be same as class attributes; i.e. name should be the same name and columns
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100))
    password=db.Column(db.String(100))

    def __init__(self,username,password): # id is a keyword so _id

        self.username=username
        self.password=password



    @classmethod #by using this calling parameter creates a new class and object; decorator to get the current class name, so that we dont have to hard code the class,self is replaced by cls
    def find_by_username(cls,username):

        return cls.query.filter_by(username=username).first() # this is class object,which creates a new class instance using db values.

    @classmethod # decorator to get the current class name, so that we dont have to hard code the class,self is replaced by cls
    def find_by_id(cls,_id):
        return cls.query.filter_by(id=_id).first() # this is class object

    def save_to_db(self):
      db.session.add(self) # adding or updating the current instance to db
      db.session.commit()