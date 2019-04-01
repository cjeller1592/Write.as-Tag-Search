from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class search(FlaskForm):
    collection = StringField('Collection', validators=[DataRequired()])
    submit = SubmitField('Submit')
