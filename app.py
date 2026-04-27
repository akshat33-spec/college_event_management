from flask import Flask
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akshat@33",
    database="college_event_system"
)

cursor = db.cursor()

@app.route('/')
def home():
    return "College Event Management Backend Running Successfully!"

if __name__ == '__main__':
    app.run(debug=True)