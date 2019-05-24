from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
    validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
    validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
    validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Create validate username function with the self, and username argument
    def validate_username(self, username):
        # if user is none then it will not the conditional and add the new account to the database
        user = User.query.filter_by(username=username.data).first()
        # if user does exist, then it will throw a ValidationError
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    # Create validate email function with the self, and email argument
    def validate_email(self, email):
        # if email is none then it will not the conditional and add the new account to the database
        email = User.query.filter_by(email=email.data).first()
        # if email does exist, then it will throw a ValidationError
        if email:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', 
    validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
    validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
    