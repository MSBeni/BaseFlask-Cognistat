from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemCheck')

    def __init__(self, name_):
        self.name = name_

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items]}

    @classmethod
    def getStorebyName(cls, name_):
        return cls.query.filter_by(name=name_).first()

    @classmethod
    def getStorebyID(cls, storeID):
        return cls.query.filter_by(id=storeID).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()