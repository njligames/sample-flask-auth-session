# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf          import FlaskForm
from flask_wtf.file     import FileField, FileRequired
from wtforms            import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired

class LoginForm(FlaskForm):
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])

class RegisterForm(FlaskForm):
	name        = StringField  (u'Name'      )
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])
	email       = StringField  (u'Email'     , validators=[DataRequired(), Email()])

class RewordMeForm(FlaskForm):
	username      = StringField  (u'Username', validators=[DataRequired()])
	email         = StringField  (u'Email'     , validators=[DataRequired(), Email()])
	password      = PasswordField(u'Password'  , validators=[DataRequired()])
	disposition   = StringField  (u'Disposition', validators=[DataRequired()])
	setup         = StringField  (u'Setup', validators=[DataRequired()])
	requestString = StringField  (u'RequestString', validators=[DataRequired()])
	responseString = StringField  (u'ResponseString')

