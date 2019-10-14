#!/usr/bin/env python
# coding: utf-8

# In[1]:
import sqlite3

from flask_restful import Resource,reqparse   # Resource class is used for methods GET,POST,PUT,DELETE

from models.user_model import UserModel

class UserRegister(Resource):
    # Since the class is being called from flask-restful add_resource method hence the class Resource is required


    def __init__(self):
        self.parser=reqparse.RequestParser() # To read the post message
        self.parser.add_argument('username',type=str,required=True,help='This field cannot be blank')
        self.parser.add_argument('password',type=str,required=True,help='This field cannot be blank')


    def post(self):

        data=self.parser.parse_args()

        # user=UserModel(data['username'],data['password'])

        user=UserModel(**data)
        user.save_to_db()
        return {'message':'User created successfully'},201


