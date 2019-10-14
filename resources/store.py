from flask_restful import Resource
from models.store_model import StoreModel

class Store(Resource):

    # def __init__(self,name):
    #     self.name=name


    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            store.json() # defult code is 200 so we dont have to retun it

        return {'message':'Store does not exist'},404 # this is a tuple that we return, dict and code after



    def post(self,name):

        if StoreModel.find_by_name(name):
            return {'message':'Store {} already exist'.format(name)},400 # this is a tuple that we return, dict and code after
        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'An error occurred while creating the store'},500

        return store.json()


    def delete(self,name):

        store=StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message':'Store deleted'}

class StoreList(Resource):

    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}



