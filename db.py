import MySQLdb

def connection():
    conn = MySQLdb.connect(host = "localhost",user = "root",password = "",db = "public_participation")

    c = conn.cursor()

    return c,conn