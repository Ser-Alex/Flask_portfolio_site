from werkzeug.security import check_password_hash
from wtforms import form, fields, validators

from portfolioapp import db
from portfolioapp.models import User


class LoginForm(form.Form):
    """
    Class to login to the admin panel
    """
    login = fields.StringField(validators=[validators.InputRequired()])
    password = fields.PasswordField(validators=[validators.InputRequired()])

    def validate_login(self, field):
        """
        Function for checking user and sending errors
        """
        from wsgi import app
        app.logger.info(msg='get started with "validate_login" functions')

        user = self.get_user()

        if user is None:
            app.logger.error(msg='The user received an error: this user does not exist!')
            raise validators.ValidationError('This user does not exist!')

        if not check_password_hash(user.password, self.password.data):
            app.logger.error(msg='The user received an error: wrong password!')
            raise validators.ValidationError('Wrong password!')

    def get_user(self):
        """
        User query from database

        :return: model User
        """
        from wsgi import app
        app.logger.warning(msg='Loading user from databases')
        return db.session.query(User).filter_by(login=self.login.data).first()