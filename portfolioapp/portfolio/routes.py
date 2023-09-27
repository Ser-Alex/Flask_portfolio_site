from flask import Blueprint, render_template
from werkzeug.exceptions import HTTPException

from portfolioapp.models import Portfolio

# create a blueprint portfolio
portfolio = Blueprint('portfolio', __name__, template_folder='templates')


@portfolio.route('/portfolio_<int:pk>', methods=['GET'])
def index_portfolio(pk):
    """
    Function to render the page
        pk: portfolio model primary key

    portfolio: model from the database for the Portfolio page,
    image_list: photos taken from portfolio
    next_portfolio: model from the database for the next Portfolio page,

    :return: rendered template
    """
    from wsgi import app
    app.logger.info(msg='get started with "index_portfolio" functions')
    try:
        portfolio = Portfolio.query.get(pk)
        app.logger.warning(msg='model loaded "portfolio"')
        image_list = [portfolio.image_2, portfolio.image_3,
                     portfolio.image_4, portfolio.image_5, portfolio.image_6,
                     portfolio.image_7, portfolio.image_8, portfolio.image_9, portfolio.image_10]
        app.logger.warning(msg='model loaded "image_list"')
    except AttributeError:
        app.logger.error(msg='Error! Portfolios are not loaded!')
        raise HTTPException('Ошибка! Портфолио не загружены!')

    image_list = [image for image in image_list if image]
    next_portfolio = Portfolio.query.get(pk + 1)
    app.logger.warning(msg='model loaded "next portfolio"')

    app.logger.info(msg='get render template')
    return render_template('portfolio/portfolio.html',
                           portfolio=portfolio,
                           next_portfolio=next_portfolio,
                           pk=pk,
                           image_list=image_list,
                           )
