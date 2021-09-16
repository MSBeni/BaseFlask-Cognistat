# from Connection.condb import Con
from db import db


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        # Con.__init__(self)
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_user_by_username(cls, username_):
        return cls.query.filter_by(username=username_).first()

        # with cls.conn() as con:
        #     result = con.execute("SELECT * FROM Users WHERE username=?", (username_,))
        #     user_ = result.fetchone()
        # if not user_:
        #     return None
        # else:
        #     fin_user = cls(*user_)
        # # connection.close()
        # return fin_user

    @classmethod
    def get_user_by_id(cls, id_):
        return cls.query.filter_by(id=id_).first()

        # with cls.conn() as con:
        #     result_ = con.execute("SELECT * FROM Users WHERE id=?", (id_,))
        #     user_ = result_.fetchone()
        # if not user_:
        #     return None
        # else:
        #     fin_user = cls(*user_)
        #
        # return fin_user
