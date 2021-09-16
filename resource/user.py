from flask_restful import reqparse, Resource
from model.user import User


class CrUser(Resource):
    # def __init__(self):
    #     Con.__init__(self)
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Add the username you want to be in the system')
    parser.add_argument('password', type=str, required=True, help='Add the password of the user')

    def post(self):
        data = CrUser.parser.parse_args()
        if User.get_user_by_username(data['username']):
            return {'message': 'user {} already exists '.format(data['username'])}

        user = User(**data)  # == User(data['username'], data['password'])
        user.save_to_db()
        # EQUAL TO:
        # with self.conn() as con:
        #     con.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (user['username'], user['password']))

        return {'message': "User {} signed up successfully".format(data['username'])}
