import os
import flask, flask_socketio, flask_sqlalchemy
import psycopg2
import chatbot


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

import models
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mkm:123@localhost/postgres'  
# db = flask_sqlalchemy.SQLAlchemy(app)

@app.route('/')
def hello():
    # messages = models.Message.query.all()
    # html = ['<li>' + m.text + '</li>' for m in messages]
    # return '<ul>' + ''.join(html) + '</ul>'
    
    
    return flask.render_template('index.html')

@socketio.on('connect') 
def on_connect():
    messages = models.Message.query.all()
    array = []
    for m in messages:
        array.append(
            [m.text]
        )
    print('Someone connected!')
    # print(array)
    socketio.emit('message array',{
     'data': array
    }, broaadcast=True)
    

    

    
    
@socketio.on('disconnect')
def on_disconnect():
    models.Message.query.delete()
    models.db.session.commit()
    print('Someone disconnected!')
    flask_socketio.emit('update', {
        'data': 'Disconnected'
    })
    
@socketio.on('new message')
def handleMessage(data):
    u_message = data['Message']
    u2_message = models.Message(data['Message'])
    #If statement for chatbot here 
    
    current_message = data['Message']

    #If it is a url, send data to the client 
    if current_message[:2] == '!!':
        called_class = chatbot.Chatbot()
        final_response = called_class.response(current_message)
        new_message = models.Message(final_response)
        models.db.session.add(new_message)
        models.db.session.commit()
   
    else:
        info = models.Message(data['Message'])
        models.db.session.add(info)
        models.db.session.commit()
    return on_connect()
    
    
    
    
    
    # models.db.session.add(u2_message)
    # models.db.session.commit()
    # print('Message: ' + u_message)
    # socketio.emit('message received', {
    #     'Message': u_message
    # })
    


if __name__ == '__main__':   
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
