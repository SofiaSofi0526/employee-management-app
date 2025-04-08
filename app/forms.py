from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class EmployeeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    salary = StringField('Salary', validators=[DataRequired()])
    submit = SubmitField('Submit')
