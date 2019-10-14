from db import db
class StoreModel(db.Model): # db.Model help to save data in SQLAlchemy

    # below rows help save the class properties to SQLAlchemy, these should be same as class attributes; i.e. name should be the same name and columns

    __tablename__='stores'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))

    items=db.relationship('ItemModel',lazy='dynamic')

    #  the code above we help to create a class instance for each row in the table; hence the names should be the same
    def __init__(self,name):
        self.name=name



    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]} # self.items.all() looks into all the items when we call json method and not create all objetcs due to lazy='dynamic'

    @classmethod # self is the instance, it will only change the instance, class method passes cls as class object
    def find_by_name(cls,name):

         return cls.query.filter_by(name=name).first() # "select * from items where name=? LIMITI =1" this returns a class object

    def save_to_db(self):
      db.session.add(self) # adding or updating the current instance to db
      db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
