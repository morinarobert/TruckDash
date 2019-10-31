# models.py
import flask_sqlalchemy, app, os


#os.environ['DATABASE_URL'] = 'postgresql://mkm003:mimcd4@localhost/postgres'
# app.app = app module app variable
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mkm:123@localhost/postgres' 
db = flask_sqlalchemy.SQLAlchemy(app.app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key
    text = db.Column(db.String(120))
    #username = db.Column(db.String(25))
    
    def __init__(self, t):
        self.text = t
        #self.username = user_name
        
    def __repr__(self):
        # return '<Message text: %s>' % self.text 
        return "<li> %s: '%s'</li>" % (self.text )