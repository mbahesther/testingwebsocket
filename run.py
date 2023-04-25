from flask import Flask, request, jsonify, json,  render_template, redirect, session,url_for
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql.cursors
import pymysql


from flask_socketio import SocketIO,send, join_room, leave_room, emit
app = Flask(__name__)


app.config['SECRECT_KEY'] = "not secure" 

socketio = SocketIO(app, manage_session=False)


config={
    'host':"",
    'user' :"",
    'password' :"F",
    'port': 3306,
    'database':"fooddevdb"
}


mydb =  pymysql.connect(**config)
cursor = mydb.cursor(pymysql.cursors.DictCursor)