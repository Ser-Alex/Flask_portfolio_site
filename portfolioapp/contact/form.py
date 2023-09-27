from wtforms import Form, TextAreaField, SubmitField, StringField, EmailField, validators


class ContactForm(Form):
    """
    Form for sending a message
    """
    name = StringField('Name', [validators.InputRequired()])
    email = EmailField('Email', [validators.Email()])
    phone = StringField('Phone', [validators.InputRequired()])
    message = TextAreaField('Message', [validators.InputRequired()])
    submit = SubmitField('Send Message')
