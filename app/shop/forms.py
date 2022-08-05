from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class SellMerchForm(FlaskForm):
    name = StringField('Product Name', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    description = StringField('Item Description', validators=[])
    img_url = StringField('IMG URL', validators=[InputRequired()])
    submit = SubmitField
