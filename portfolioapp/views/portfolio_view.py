import os

from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

file_path = os.path.abspath(os.path.dirname(__name__))


class PortfolioView(ModelView):
    """
    View model class portfolio for the admin panel
    """
    can_delete = True
    can_edit = True
    can_create = True

    create_modal = True
    edit_modal = True

    form_extra_fields = dict()
    for num in range(10):
        image_num = f'image_{num+1}'

        # ImageUploadField Performs image verification, thumbnail creation, updating, and deleting of images.
        form_extra_fields[image_num] = form.ImageUploadField(
            image_num, base_path=os.path.join(file_path, f'portfolioapp/static/images/portfolio/'))

    # then there are functions for making changes in a separate window
    def create_form(self, obj=None):
        from wsgi import app
        app.logger.warning(msg='create form portfolio')
        return super(PortfolioView, self).create_form(obj)

    def edit_form(self, obj=None):
        from wsgi import app
        app.logger.warning(msg='edit form portfolio')
        return super(PortfolioView, self).edit_form(obj)

    def is_accessible(self):
        from wsgi import app
        app.logger.warning(msg='authenticated user')
        return current_user.is_authenticated