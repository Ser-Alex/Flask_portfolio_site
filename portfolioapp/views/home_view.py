import os

from flask import url_for
from flask_admin import form
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from markupsafe import Markup

from portfolioapp.views import file_path


class HomeView(ModelView):
    """
    View model class home for the admin panel
    """
    can_delete = False
    can_edit = True
    can_create = True

    create_modal = True
    edit_modal = True

    def _list_thumbnail(view, context, model, name):
        """
        function for saving a small photo

        :return: if there is a photo, it saves its small photo, if not, then None
        """
        if not model.image:
            return ''

        url = url_for('static', filename=os.path.join('images/home/', model.image))
        if model.image.split('.')[-1] in ['jpg', 'jpeg', 'png', 'svg', 'gif']:
            return Markup(f'<img src={url} width="100">')

    column_formatters = {
        'image': _list_thumbnail
    }

    form_extra_fields = {
        # ImageUploadField Performs image verification, thumbnail creation, updating, and deleting of images.
        "image": form.ImageUploadField(
            '',
            base_path=os.path.join(file_path, 'portfolioapp/static/images/home/'),
            allowed_extensions=['jpg'],
            thumbnail_size=(100, 100, True),
        )
    }

    # then there are functions for making changes in a separate window
    def create_form(self, obj=None):
        from wsgi import app
        app.logger.warning(msg='create form home')
        return super(HomeView, self).create_form(obj)

    def edit_form(self, obj=None):
        from wsgi import app
        app.logger.warning(msg='edit form home')
        return super(HomeView, self).edit_form(obj)

    def is_accessible(self):
        from wsgi import app
        app.logger.warning(msg='authenticated user')
        return current_user.is_authenticated