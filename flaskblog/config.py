# config file will be class based - this will allow us to have all of our configuration contained in a single object and allow us to use Inheritance to create new configurations and other things of that nature . . .
import os

class Config:
    # paste all our current configurations from our __init__.py file
    # all the constants that start with app.config should be placed here
    # now we don't need the app.config parts of code and can just use the constant variable names by themselves like so 

    '''it used to be: app.config['SECRET_KEY'] = ...'''

    # now lets also use an environment variable for our SECRET_KEY and SQLALCHEMY_DATABASE_URI
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')