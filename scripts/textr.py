import os
import flask, flask_socketio, flask_sqlalchemy
import psycopg2
import models

def hello():
    messages = models.Message.query.all()
    html = ['<li>' + m.text + '</li>' for m in messages]
    return '<ul>' + ''.join(html) + '</ul>'