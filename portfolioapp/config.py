import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SQLALCHEMY_DATABASE_URI = "sqlite:///app_db.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.urandom(20)
FLASK_ADMIN_SWATCH = 'cosmo'

MAIL_SERVER = 'smtp.yandex.ru'
MAIL_PORT = 465
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = os.environ.get("MAIL_USERNAME")
MAIL_USE_TLS = False
MAIL_USE_SSL = True

