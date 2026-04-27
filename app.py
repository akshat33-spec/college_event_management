from flask import Flask
import os
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)
import os

db = mysql.connector.connect(
    host=os.getenv("MYSQLHOST"),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQLDATABASE"),
    port=int(os.getenv("MYSQLPORT"))
)


cursor = db.cursor()

@app.route('/')
def home():
    return "College Event Management Backend Running Successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)