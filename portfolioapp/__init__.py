import os

import sentry_sdk
from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sentry_sdk.integrations.flask import FlaskIntegration

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()


def create_app():
    # Sentry connections
    sentry_sdk.init(
        dsn=os.environ.get("SENTRY_KEY"),
        integrations=[FlaskIntegration()],
    )

    # creating a flask application
    app = Flask(__name__)
    app.logger.warning(msg='create app')

    # connecting additional modules
    app.config.from_pyfile("config.py")
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    login_manager.init_app(app)
    app.logger.warning(msg='connecting additional modules')

    from portfolioapp.admin.routes import MyAdminIndexView
    from .models import User, Home, Portfolio, Contact, Photo, About, Skill

    # creating an admin panel
    admin = Admin(app, "Wedding", index_view=MyAdminIndexView(), base_template='my_master.html', template_mode='bootstrap4', url='/')
    app.logger.warning(msg='creating an admin panel')

    from portfolioapp.views.home_view import HomeView
    from portfolioapp.views.portfolio_view import PortfolioView
    from portfolioapp.views.contact_view import ContactView
    from portfolioapp.views.about_view import AboutView
    from portfolioapp.views.photo_view import PhotoView
    from portfolioapp.views.about_view import AboutView
    from portfolioapp.views.skill_view import SkillView
    from portfolioapp.views.user_view import UserView

    # connecting modules to the admin panel
    admin.add_view(HomeView(Home, db.session, endpoint='admin/home'))
    admin.add_view(PhotoView(Photo, db.session, endpoint='admin/photo'))
    admin.add_view(PortfolioView(Portfolio, db.session, endpoint='admin/portfolio'))
    admin.add_view(ContactView(Contact, db.session, endpoint='admin/contact'))
    admin.add_view(AboutView(About, db.session, endpoint='admin/about'))
    admin.add_view(SkillView(Skill, db.session, endpoint='admin/skill'))
    admin.add_view(UserView(User, db.session, endpoint='admin/user'))
    app.logger.warning(msg='connecting modules to the admin panel')

    from portfolioapp.home.routes import home
    from portfolioapp.portfolio.routes import portfolio
    from portfolioapp.contact.routes import contact
    from portfolioapp.about.routes import about

    # register blueprint
    app.register_blueprint(home)
    app.register_blueprint(portfolio)
    app.register_blueprint(contact)
    app.register_blueprint(about)
    app.logger.warning(msg='register blueprint')

    # register command
    from portfolioapp.command import user_cli
    app.cli.add_command(user_cli)
    app.logger.warning(msg='register command')

    # connecting user
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

    return app
