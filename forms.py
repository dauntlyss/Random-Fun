from flask_wtf import FlaskForm
from wtforms import SelectField, BooleanField, DecimalField
from wtforms.validators import NumberRange

# ---May use to allow user to add activites to db---
# class MessageForm(FlaskForm):
#     """Form for adding/editing messages."""

#     text = TextAreaField('text', validators=[DataRequired()])

TYPES = [('All', 'All'), ('Busywork', 'Busywork'), ('Charity', 'Charity'), ('Cooking', 'Cooking'), ('DIY', 'DIY'), ('Music', 'Music'), ('Recreational', 'Recreational'), ('Relaxation', 'Relaxation'), ('Social', 'Social')
]
class GenerateActivityForm(FlaskForm):
    """Form for generating activities."""

    activity = SelectField("Type", choices=TYPES)
    minprice = DecimalField("Minimum Price", validators=[NumberRange(min=0, max=1, message='value between 0 and 1')],render_kw={"placeholder": "0-1"} )
    accessible = BooleanField("Accessible Activity")

# class UserEditForm(FlaskForm):
#     """Form for editing existing users."""
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('E-mail', validators=[DataRequired(), Email()])
#     image_url = StringField('(Optional) Image URL')
#     header_image_url = StringField('(Optional) Header Image URL')
#     bio = TextAreaField('(Optional) Add a bio')
#     location = TextAreaField('(Optional) Where are you?')
#     password = PasswordField('Password', validators=[Length(min=6)])


# class LoginForm(FlaskForm):
#     """Login form."""

#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[Length(min=6)])
