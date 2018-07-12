from flask import Flask, request, jsonify, session
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
import mysqldb
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

api = Api(app, prefix="/api/v1")

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    returned_data = mysqldb.getLoginUser(username)
    returned_username = returned_data[1]
    returned_password = returned_data[0]
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username == returned_username and bcrypt.checkpw(password.encode('utf-8'), returned_password.encode('utf-8')):
        access_token = create_access_token({'first_name': request.json.get('Client First Name', None), 'last_name': request.json.get('Client Last Name', None), 'user_name': request.json.get('Username', None), 'user_password': request.json.get('Password', None)})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401

class PrivateResource(Resource):
    @app.route('/protected', methods=['GET'])
    @jwt_required

    def sendData():
        data = get_jwt_identity()
        return mysqldb.addUser("{}".format(str(data['first_name'])),"{}".format(str(data['last_name'])))

class PasswordResource(Resource):
    @app.route('/register', methods=['GET'])
    @jwt_required

    def sendPassword():
        data = get_jwt_identity()
        hashed_password = bcrypt.hashpw(data['user_password'].encode('utf8'), bcrypt.gensalt())
        return mysqldb.addPassword("{}".format(str(data['user_name'])),"{}".format(hashed_password))


if __name__ == '__main__':
    app.run(debug=True)