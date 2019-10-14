#!/usr/bin/env python
# coding: utf-8

# In[8]:


from models.user_model import UserModel


def authenticate(username,password):
    user=UserModel.find_by_username(username) # .get function gives elements of a dictionary on key;None os the default value
    if user and user.password==password:
        return user
    
    
def identity(payload):
    user_id=payload['identity'] # ['identity is the first element of the payload]
    return UserModel.find_by_id(user_id)
    
    

