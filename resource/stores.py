from flask_restful import Resource
from model.stores import StoreModel


class StoreRes(Resource):
    def get(self, name):
        if not StoreModel.getStorebyName(name):
            return {'message': 'Store {} not found. '.format(name)}, 404

        return StoreModel.getStorebyName(name).json()

    def post(self, name):
        if StoreModel.getStorebyName(name):
            return {'message': 'Store {} already exists. '.format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'There is something wrong with DB. '}, 500

    def put(self, name):
        pass

    def delete(self, name):
        if not StoreModel.getStorebyName(name):
            return {'message': 'Such a store named {} not found. '.format(name)}, 404

        StoreModel.getStorebyName(name).delete_from_db()


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}


class StoreName(Resource):
    def get(self, storeID):
        if not StoreModel.getStorebyID(storeID):
            return {'message': 'Store {} not found. '.format(storeID)}, 404

        return StoreModel.getStorebyID(storeID).json()
