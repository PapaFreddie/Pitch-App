from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField, ValidationError
from wtforms.validators import Required,Email,Length,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(),
    EqualTo('password',message = 'Password should match')])
    password2 = PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Sign Up')

#validators
    def validate_email(self,data_field):
        if User.query.filter_by(email =data_field.data).first():
            raise ValidationError('Account already exixsts! Please creat another account by signing up!')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username exists! Please use another username')