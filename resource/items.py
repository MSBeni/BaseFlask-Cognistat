from flask_restful import reqparse, Resource
# from flask import jsonify
from flask_jwt import jwt_required
from model.items import ItemCheck
# from sqlalchemy import create_engine
# from Connection.condb import Con
# import json


class Item(Resource):
    # def __init__(self):
    #     Con.__init__(self)
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="Add the Price of new Item")
    parser.add_argument('store_id', type=float, required=True, help="Every item need a store id")

    @jwt_required()
    def get(self, name):
        item = ItemCheck.getItembyName(name)
        if item:
            return item.json()
        return {'message': 'Item {} Do not exists'.format(name)}, 400

    def post(self, name):
        if ItemCheck.getItembyName(name):
            return {'message': 'Item {} already exists'.format(name)}, 400

        data = Item.parser.parse_args()

        # item = ItemCheck(name, data['price'], data['store_id'])
        item = ItemCheck(name, data['price'], data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the new item ..."}, 500

        return item.json(), 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemCheck.getItembyName(name)
        if not item:
            return {'message': 'Item {} does not exist'.format(name)}, 400

        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()


    def delete(self, name):
        item = ItemCheck.getItembyName(name)
        if item:
            ItemCheck.delete_from_db()
        return {'message': 'Item {} is deleted successfully'.format(name)}, 201


class AddItem(Resource):
    # def __init__(self):
    #     Con.__init__(self)

    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name of the Item')
    parser.add_argument('price', type=str, required=True, help='Name of the Item')

    def post(self):
        data = AddItem.parser.parse_args()
        if ItemCheck.getItembyName(data['name']):
            return {'message': 'Item {} already exists'.format(data['name'])}, 400

        ItemCheck.save_to_db(**data)

        # with self.conn() as con:
        #     con.execute("INSERT INTO Items VALUES (?, ?)", (data['name'], data['price']))

        return {'message': 'Item {} is added successfully'.format(data['Name'])}, 201


class AllItems(Resource):
    # def __init__(self):
    #     Con.__init__(self)
    def get(self):
        # return {'items': list(map(lambda x: x.json(), ItemCheck.query.all()))}
        return {'item': [x.json() for x in ItemCheck.query.all()]}
        # with self.conn() as con:
        #     Items_ = con.execute("SELECT * FROM Items").fetchall()
        #
        # result = jsonify({'result': [dict(row) for row in Items_]})
        # return result if Items_ else 404