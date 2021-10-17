import os
import re
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import json
from security import auth_, identity
from resource.items import Item, AddItem, AllItems
from resource.user import CrUser
from resource.stores import StoreRes, StoreList, StoreName
# from create_drop_tables import Tables
from db import db


app = Flask(__name__)

# Server pass - local or Cloud
# password_db = json.loads(open('secretfiles.json', 'r').read())['web']['user_pw']

# SQL Server Config - Local
# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://sa:" + password_db + "@localhost:1433/testDB?driver=ODBC+Driver+17+for+SQL+Server"

# SQLite Config - Heroku
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# Postgres Config - Heroku
uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

# rest of connection code using the connection string `uri`
app.config['SQLALCHEMY_DATABASE_URI'] = uri


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

# Test on Heroku
app.secret_key = 'msbeni'

# Local Secret Key
# app.secret_key = json.loads(open('authAPP.json', 'r').read())['auth']['api_secret']
api = Api(app)

jwd = JWT(app, auth_, identity)

api.add_resource(Item, '/items/<string:name>')
api.add_resource(AddItem, '/items/Add')
api.add_resource(AllItems, '/items')
api.add_resource(CrUser, '/signup')
api.add_resource(StoreRes, '/stores/<string:name>')
api.add_resource(StoreName, '/storeName/<string:storeID>')
api.add_resource(StoreList, '/stores')

# Tables.drop_or_create_tables()

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
