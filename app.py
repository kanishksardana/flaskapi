#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

import os
from security import authenticate,identity
from resources.user import  UserRegister
from resources.item import Item,Items
from resources.store import Store,StoreList

app=Flask(__name__)  # app will use the flask


app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL','sqlite:///data.db')  # you can use any database with sqlalchemy, i.e. oracle,etc
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # its improves performance; this Turns off Flasks sql alchemy tracker as now SQLAlchemy module has its own tracker.

app.secret_key='jose'

api=Api(app) # to use flask_restful; api object will work with app object from Flask class




"""
JWT function will first call authenticate function and create a JWT token,
then idenity function uses the JWT token and checks if the id exists for the same token.
"""

jwt=JWT(app,authenticate,identity) # creates and calls a new endpoint /auth


#  Below are the enpoints ; methods are defined within the class, eg: get,post,delete,put etc.

api.add_resource(Item,'/item/<string:name>')  # api restful accepts class and string as parameter
api.add_resource(Items,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')


if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(port=9000,debug=True) # app.run should execute when we run directly and dont iport it





