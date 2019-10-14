from db import db
class ItemModel(db.Model): # db.Model help to save data in SQLAlchemy

    # below rows help save the class properties to SQLAlchemy, these should be same as class attributes; i.e. name should be the same name and columns

    __tablename__='items'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    price=db.Column(db.Float(precision=2))


    store_id=db.Column(db.Integer,db.ForeignKey('stores.id')) # store id column from the stores

    store=db.relationship('StoreModel')

    #  the code above we help to create a class instance for each row in the table; hence the names should be the same
    def __init__(self,name,price,store_id):
        self.name=name
        self.price=price
        self.store_id=store_id

    def json(self):
        return {'name':self.name,'price':self.price}

    @classmethod # self is the instance, it will only change the instance, class method passes cls as class object
    def find_by_name(cls,name):

         return cls.query.filter_by(name=name).first() # "select * from items where name=? LIMITI =1" this returns a class object

    def save_to_db(self):
      db.session.add(self) # adding or updating the current instance to db
      db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
