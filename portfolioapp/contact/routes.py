from flask import Blueprint, render_template, request, flash
from flask_mail import Message

from portfolioapp import mail
from portfolioapp.contact.form import ContactForm
from portfolioapp.models import Contact, User

# create a blueprint contact
contact = Blueprint('contact', __name__, template_folder='templates')


@contact.route('/contact', methods=['GET', 'POST'])
def index_contact():
    """
    function for rendering pages, in the case of a post request,
    sending the form by email

    contact: model from the database for the Contact page,
    form: form on page

    :return: rendered template
    """
    from wsgi import app
    app.logger.info(msg='get started with "admin_conntact" functions')

    contact = Contact.query.get(1)
    app.logger.warning(msg='Contact model requested')

    form = ContactForm(request.form)
    app.logger.warning(msg='Getting a form from a request')

    if request.method == 'POST':
        app.logger.warning(msg='Post method')

        if form.validate() == True:
            app.logger.warning(msg='the form is valid, sending a message')
            msg = Message('Yor title text', sender='your email', recipients=[User.query.get(1).email])
            msg.body = f'name: {form.name.data}, phone: {form.phone.data}, email: {form.email.data} ' \
                       f'text: {form.message.data}'
            mail.send(msg)
            flash('The form has been sent, please wait for a response.')
            app.logger.info(msg='letter sent')
        else:
            app.logger.warning(msg='Form filling error')
            flash('Data error! Form not sent!')

    app.logger.info(msg='Get render template')
    return render_template('contact/contact.html', form=form, contact=contact)
