import sqlite3
from db import db
class ItemModel(db.Model): # db.Model help to save data in SQLAlchemy

    # below rows help save the class properties to SQLAlchemy, these should be same as class attributes; i.e. name should be the same name and columns

    __tablename__='items'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    price=db.Column(db.Float(precision=2))

    #  the code above we help to create a class instance for each row in the table; hence the names should be the same
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod # self is the instance, it will only change the instance, class method passes cls as class object
    def find_by_name(cls,name):

        # Below code is for SQLite
            # connection=sqlite3.connect('data.db')
            # cursor=connection.cursor()
            #
            # select_item_query="select * from items where name=?"
            #
            # result=cursor.execute(select_item_query,(name,))
            #
            # row=result.fetchone()
            # connection.close()
            # if row:
            # # return cls(row[0],row[1]) # this cls will call class item model and construct and return a class object of ItemModel
            #     return cls(*row) # same as above

        # The above code in sqllite can be replace in SQLAlchemy as following, no connection etc is required:

        # return ItemModel.query.filter_by(name=name).filter_by(id=1)
          return cls.query.filter_by(name=name).first() # "select * from items where name=? LIMITI =1" this returns a class object






    def save_to_db(self):

        # connection=sqlite3.connect('data.db')
        # cursor=connection.cursor()
        #
        # insert_item_query="Insert into  items  values(?,?)"
        #
        # result=cursor.execute(insert_item_query,(self.name,self.price,))
        #
        # connection.commit()
        # connection.close()
    #     SQLAlchemy makes it simple

        db.session.add(self) # adding the
        db.session.commit()




    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
