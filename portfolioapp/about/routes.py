from flask import Blueprint, render_template

from portfolioapp.models import About, Skill

# create a blueprint about
about = Blueprint('about', __name__, template_folder='templates')


@about.route('/about', methods=['GET'])
def index_about():
    """
    Function to render the page

    about_me: model from the database for the about_me page,
    skill_list: model from the database for the skill_list page

    :return: rendered template
    """
    from wsgi import app
    app.logger.info(msg='get started with "about" functions')

    about_me = About.query.get(1)
    app.logger.warning(msg='model loaded "about_me"')

    skill_list = Skill.query.all()
    app.logger.warning(msg='model loaded "skill_list"')

    return render_template('about/about.html',
                           about=about_me,
                           skill_list=skill_list,
                           )
