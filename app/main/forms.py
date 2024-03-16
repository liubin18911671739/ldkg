from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    query = StringField("搜索", validators=[DataRequired()])
    submit = SubmitField("搜索")
