from flaskblog import db, login_manager, app
from flask_login import UserMixin
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # create a new method like so (1800 seconds = 30 mins)
    def get_reset_token(self, expires_sec=1800):
        # create a Serializer object
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        # return token that we created which contains a payload of the current user id
        return s.dumps({'user_id': self.id}).decode('utf-8')

    # decorator to tell that this is a static method because we don't need the self argument
    @staticmethod
    # create a method that verifies the token
    def verify_reset_token(token):
        # create serializer object without expired seconds
        s = Serializer(app.config['SECRET_KEY'])
        # put it in a try / except block because the token might be expired
        try:
            # try to get user_id (comes out of the payload) from the token 
            user_id = s.loads(token)['user_id']
        except:
            return None
        # if we don't get an exception then it will return that user_id
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
