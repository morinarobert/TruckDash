import os
import flask, flask_socketio, flask_sqlalchemy
import psycopg2


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

import models
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mkm:123@localhost/postgres'  
db = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/')
def hello():

    
    return flask.render_template('index.html')

@socketio.on('connect') 
def on_connect():
    print('Someone connected!')
    flask_socketio.emit('update', {
        'data': 'Got your connection!'
    })
    
@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')
    flask_socketio.emit('update', {
        'data': 'Disconnected'
    })
    
@socketio.on('message')
def handleMessage(msg):
    u_message = msg['Message']
    
    print('Message: ' + u_message)
    socketio.emit(u_message, broadcast=True)
    models.db.session.add(u_message)
    models.db.session.commit()

    
@socketio.on('new number')
def on_new_number(data):
    print ("Got an event for new number with data:", data)
    rand_number = data['number']
    socketio.emit(rand_number, broadcast=True)

if __name__ == '__main__':   
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
