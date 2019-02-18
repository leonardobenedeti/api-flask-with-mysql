from flask import Flask, jsonify
from flask.ext.mysql import MySQL 

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'b45fc1daa17d12'
app.config['MYSQL_DATABASE_PASSWORD'] = '910f54a1'
app.config['MYSQL_DATABASE_DB'] = 'heroku_428b368c435e5d2'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-iron-east-03.cleardb.net'
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
