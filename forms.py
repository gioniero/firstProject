from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from models import User


class SignupForm(FlaskForm):
    email = StringField('Your email', validators=[DataRequired(), Email()])
    username = StringField('Your username', validators=[DataRequired()])
    password = PasswordField('Your password', validators=[DataRequired(), EqualTo('confirm_password', "Password must match")])
    confirm_password = PasswordField('Confirm password')
    submit = SubmitField('Sign up')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('This email already exists.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username already exists.')


class LoginForm(FlaskForm):
    email = StringField('Your email', validators=[DataRequired(), Email()])
    password = PasswordField('Your password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')
