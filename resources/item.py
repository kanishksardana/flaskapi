from flask import request
from flask_restful import Resource,reqparse
from flask_jwt import JWT,jwt_required

from models.item_model import ItemModel

class Items(Resource):

    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}


class Item(Resource):  # student in the endpoint ; class inheritence student class will get all the methods from Resource class

    def __init__(self):

        self.parser=reqparse.RequestParser()
        self.parser.add_argument('price',type=float,required=True,help='This field cannot be left blank')
        self.parser.add_argument('store_id',type=int,required=True,help='Every Item needs a store id kanishk')

    @jwt_required() # this decorator check the authentication token
    def get(self,name):  # from resource we will only use get method

        item=ItemModel.find_by_name(name)
        if item:
            return item.json()

        return {'message':'Item not found'},404


    def post(self,name):

        if ItemModel.find_by_name(name):
            return{"message": "An item with the name {} already exists".format(name)},400 # bad request
        data=self.parser.parse_args()
        # item={"name":name, "price":data["price"]}
        item=ItemModel(name,data["price"],data['store_id']) # item becomes object of class ItemModel
        # exception handling: if database insert fails; try inserting if exception occurred then the except return message

        try:

            # ItemModel.insert(item)
            item.save_to_db() # calling object above

        except:
            return {"message":"An error occurred while inserting the item."},500 # Internal server error


        return item.json(),201 # new item created; always return json

    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db(name)



        return {'message':'item deleted'}



    def put(self,name):

        # data=request.get_json()
        data=self.parser.parse_args()
        item=ItemModel.find_by_name(name)
        # updated_item=ItemModel(name,data["price"])
        if item is None:
            # item=ItemModel(name,data['price'],data['store_id'])
            item=ItemModel(name,**data)
        else:
            item.price=data['price']

        item.save_to_db()

        return item.json()


