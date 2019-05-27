from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

# remove the app variable from the initializations
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

# create a function that takes an argument  for what configuration object we want to use in our application
# Config is what we imported from config.py class
def create_app(config_class=Config):
    # now we're going to move the creation of our application inside of this create_app( ) function
    # the extensions will remain outside of the function
    # we're going to initialize the extensions at the top of our file but without the app variable
    app = Flask(__name__)
    app.config.from_object(Config)

    # copy and paste the extensions in here 
    # for each of these functions we will run the .init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    # return the application
    return app