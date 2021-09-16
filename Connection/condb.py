from sqlalchemy import create_engine
import json

class Con:
    @staticmethod
    def conn():
        password_db = json.loads(open('../../../secretfiles.json', 'r').read())['web']['user_pw']
        engine = create_engine(
            "mssql+pyodbc://sa:" + password_db + "@localhost:1433/testDB?driver=ODBC+Driver+17+for+SQL+Server")
        connection = engine.connect()
        return connection
    # password_db = json.loads(open('../../../secretfiles.json', 'r').read())['web']['user_pw']
    # engine = create_engine(
    #     "mssql+pyodbc://sa:" + password_db + "@localhost:1433/testDB?driver=ODBC+Driver+17+for+SQL+Server")
    # connection = engine.connect()