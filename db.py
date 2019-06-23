from Flask import Flask,jsonify,request,json
from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token


app = Flask(__name__);

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '';
app.config['DB_NAME'] = 'public_participation'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'



mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)