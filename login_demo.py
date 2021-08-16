from flask import Flask, render_template, url_for, request, session, redirect
from flask.ext.pymongo import PyMongo
import bcrypt

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mongodbdemo'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mongodbdemo'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return 'You are '

if __name__=='__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
