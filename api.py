from flask import Flask, jsonify
from flask.ext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'USER'
app.config['MYSQL_DATABASE_PASSWORD'] = 'PASS'
app.config['MYSQL_DATABASE_DB'] = 'DB'
app.config['MYSQL_DATABASE_HOST'] = 'HOST'
mysql.init_app(app)


# routes
@app.route('/', methods=["GET", ])
def index():
    conn = mysql.connect()
    cursor = conn.cursor()
    signin = cursor.execute("SELECT * FROM TABLE")
    signin = cursor.fetchone()

    conn.close()
    return jsonify(signin)


if __name__ == "__main__":
    app.run(debug=True)
