from flask import Blueprint, render_template

from portfolioapp.models import Home, Photo


home = Blueprint('home', __name__, template_folder='templates')


@home.route('/', methods=['GET'])
def index_home():
    """
    Function to render the page

    home: model from the database for the Home page,
    image: model from the database for the Photo page

    :return: rendered template
    """
    from wsgi import app
    app.logger.info(msg='get started with "index_home" functions')

    home = Home.query.get(1)
    app.logger.warning(msg='model loaded "home"')

    image = Photo.query.all()
    app.logger.warning(msg='model loaded "image"')

    app.logger.info(msg='get render template')
    return render_template('home/index.html', home=home, image_list=image)
