from sqlalchemy import create_engine
import json
# from Connection.condb import Con
from db import db


class ItemCheck(db.Model):
    __tablename__ = 'Items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name_, price_, store_id):
        self.name = name_
        self.price = price_
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    @classmethod
    def getItembyName(cls, name_):
        return cls.query.filter_by(name=name_).first()
        # with cls.conn() as con:
        #     item = con.execute("SELECT * FROM Items WHERE name=?", (name_, )).fetchone()
        #     if item:
        #         return item
        #     else:
        #         return None

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()