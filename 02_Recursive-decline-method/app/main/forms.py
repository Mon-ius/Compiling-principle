from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,\
                    BooleanField, TextAreaField
from wtforms.validators import DataRequired,ValidationError,Length
from flask_babel import _, lazy_gettext as _l

class PostForm(FlaskForm):
    post = TextAreaField(_l('Input'), validators=[DataRequired()])
    
    submit = SubmitField(_l('Translate'))