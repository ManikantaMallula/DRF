from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, EqualTo



class AddItemForm(FlaskForm):
    Fooditem = StringField(validators=[DataRequired(), Length(min=1, max=6)])
    quantity = StringField(validators=[DataRequired(), Length(min=1, max=6)])
    calories = StringField(validators=[DataRequired(), Length(min=1, max=6)])
    fat = StringField(validators=[DataRequired(), Length(min=1, max=6)])
    carbohydrates = StringField(validators=[DataRequired(), Length(min=1, max=6)])
    protein = StringField(validators=[DataRequired(), Length(min=1, max=6)])
    category = StringField(validators=[DataRequired(), Length(min=1, max=6)])
    submit = SubmitField('add')

class AddDateForm(FlaskForm):
    date = DateField(format='%m%d%y', validators=[DataRequired()])
    submit = SubmitField('create')


# class AddDetailForm(FlaskForm):
#     add_item =
#     date_d =



