import click
from flask.cli import AppGroup
from werkzeug.security import generate_password_hash

from portfolioapp import db
from portfolioapp.models import User

user_cli = AppGroup('user')


@user_cli.command('create')
@click.argument('login')
@click.argument('password')
@click.argument('email')
def create_user(login, password, email):
    """
    command to create user

    :param login: login is transmitted
    :param password: password is transmitted
    :param email: email is transmitted, to send messages
    """
    from wsgi import app
    app.logger.info(msg='start func "create user"')

    user = User(login=login, password=generate_password_hash(password), email=email)
    app.logger.info(msg=f'User create {user.login}')

    db.session.add(user)
    db.session.commit()
    app.logger.info(msg='saving the user to the database')

    print(f'Create user - {login}')