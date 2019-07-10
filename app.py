from flask import Flask, jsonify, request, json
from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt, check_password_hash
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

from db import connection


app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'my_only_secret'


jwt = JWTManager(app)
bcrypt = Bcrypt(app)
CORS(app)


@app.route('/auth/register', methods=['POST'])
def register():

    c, conn = connection()

    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(
        request.get_json()['password']).decode('utf-8')
    created_at = datetime.utcnow()

    if not validateuser(email):
        c.execute("INSERT INTO users (first_name, last_name, email, password, created_at) VALUES ('" +
                  str(first_name) + "', '" +
                  str(last_name) + "', '" +
                  str(email) + "', '" +
                  str(password) + "', '" +
                  str(created_at) + "')")
        conn.commit()

        result = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'created_at': created_at
        }

        return jsonify({'result': result})
    else:
        ##Username Already Exist.....
         result = jsonify({'result': 1})

         return result




@app.route('/auth/login', methods=['POST'])
def login():
    c,conn = connection()
    email = request.get_json()['email']
    password = request.get_json()['password']
    result = ""

    c.execute("SELECT * FROM users where email = '" + str(email) + "'")
    rv = c.fetchone()

    if bcrypt.check_password_hash(rv[4], password):
        access_token = create_access_token(
            identity={'first_name': rv[1], 'last_name': rv[2], 'email': rv[3]})
        result = access_token
    else:
        result = jsonify({"error": "Invalid username and password"})

    return result


def validateuser(email):
    c,conn = connection()
   ## email = request.get_json()['email']

    c.execute("SELECT * from users WHERE email = '" + str(email) + "'")
    data = c.fetchone()

    return data


if __name__ == '__main__':
    app.run(debug=True)
