from flask import Flask, request, jsonify, session
from flask_restful import Resource, Api
from werkzeug.security import generate_password_hash, check_password_hash
import mysqldb
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

api = Api(app, prefix="/api/v1")

USER_DATA = {
    "user1": "abc123",
    "user2":"userpass"
}

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != USER_DATA.get(username) and password not in USER_DATA[username]:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token({'first_name': request.json.get('Client First Name', None), 'last_name': request.json.get('Client Last Name', None)})
    return jsonify(access_token=access_token), 200

class PrivateResource(Resource):
    @app.route('/protected', methods=['GET'])
    @jwt_required

    def sendData():
        data = get_jwt_identity()
        return mysqldb.addUser("{}".format(str(data['first_name'])),"{}".format(str(data['last_name'])))



#api.add_resource(PrivateResource, '/private')

if __name__ == '__main__':
    app.run(debug=True)