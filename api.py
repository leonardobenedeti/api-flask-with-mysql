from flask import Flask, jsonify
from flask.ext.mysql import MySQL 

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations  #### REVER trecho de configuração para buscar as informações
app.config['MYSQL_DATABASE_USER'] = 'USER'
app.config['MYSQL_DATABASE_PASSWORD'] = 'PASSWD'
app.config['MYSQL_DATABASE_DB'] = 'DEFAULT_SCHEMA'
app.config['MYSQL_DATABASE_HOST'] = 'HOST'
mysql.init_app(app)


# routes
@app.route('/', methods=["GET", ])
def index():
    conn = mysql.connect()
    cursor = conn.cursor()
    users = cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    conn.close()
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
