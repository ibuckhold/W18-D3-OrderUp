from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField,
    SubmitField,
    PasswordField
)
from wtforms.validators import (
    DataRequired,
    ValidationError
)


class LoginForm(FlaskForm):
    employee_number = StringField('Employee Number')
    password = PasswordField('Password')
    submit = SubmitField('Login')
