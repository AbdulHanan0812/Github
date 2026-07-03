from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

# 🌟 Spelling Check: Pura naam 'Registration_form' hona chahiye
class Registration_form(FlaskForm):
    name = StringField("Full Name:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField("Password:", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Register Here")


class Login_form(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("Login")