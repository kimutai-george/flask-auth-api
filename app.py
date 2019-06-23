from flask import Flask,jsonify,request,json
from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt,check_password_hash
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token


app = Flask(__name__);


app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
##app.config['MYSQL_PASSWORD'] = ''
app.config['DB_NAME'] = 'public_participation'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'



mysql = MySQL(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)


@app.route('/auth/register', methods =  ['POST'])
def register():
	request.get_json(force=True)
	cur = mysql.connection.cursor();

	first_name = request.get_json()['first_name']
	last_name = request.get_json()['last_name']
	email = request.get_json()['email']
	password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
	created_at = datetime.utcnow()

	cur.execute("INSERT INTO `public_participation`.`users` (first_name,last_name,email,password,created_at) VALUES ('"+
		str(first_name)+ "','"+
		str(last_name)+ "','"+
		str(email)+ "','"+
		str(password)+ "','"+
		str(created_at)+ "')")

	mysql.connection.commit()

	result = {
	"first_name" : first_name,
	"last_name" : last_name,
	"email" : email,
	"password" : password,
	"created_at" : created_at
	}


	return jsonify({"result" : result})


@app.route('/auth/login', methods = ['POST'])
def login():
	request.get_json(force=True)
	cur = mysql.connection.cursor();

	email = request.get_json()['email']
	password = request.get_json()['password']
	result = ""

	cur.execute("SELECT * FROM `public_participation`.`users` WHERE email = '"+ str(email) +"'")
	fn = cur.fetchone()
	if fn:
		passd = fn['password']
		if check_password_hash(passd,password):
			access_token = create_access_token(identity = {'first_name' : fn['first_name'],'last_name' : fn['last_name'],'email' : fn['email']})
			result = jsonify({'token' : access_token})
		else:
			result = jsonify({'error' : "Invalid Username or password"})
	else:
		result = jsonify({'error' : "No records were found"})



	return result


if __name__ == '__main__':
	app.run(debug = True)


