import os
import flask, flask_socketio, flask_sqlalchemy
import psycopg2


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

import models
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mkm:123@localhost/postgres'  
# db = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/')
def hello():

    
    return flask.render_template('index.html')

@socketio.on('connect') 
def on_connect():
    messages = models.Message.query.all()
    print(messages)
    array = []
    for m in messages:
        array.append(
            [m.text]
        )
    
    
    print('Someone connected!')
    print(array)
    socketio.emit('message received',{
     'data': array
    }, broaadcast=True)
    
@socketio.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')
    flask_socketio.emit('update', {
        'data': 'Disconnected'
    })
    
@socketio.on('new message')
def handleMessage(data):
    u_message = data['Message']
    u2_message = models.Message(data['Message'])
    models.db.session.add(u2_message)
    models.db.session.commit()
    print('Message: ' + u_message)
    socketio.emit('message received', {
        'Message': u_message
    })
    


if __name__ == '__main__':   
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
