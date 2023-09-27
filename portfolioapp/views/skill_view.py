from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class SkillView(ModelView):
    """
    View model class skill for the admin panel
    """
    can_delete = True
    can_edit = True
    can_create = True

    create_modal = True
    edit_modal = True

    # then there are functions for making changes in a separate window
    def create_form(self, obj=None):
        from wsgi import app
        app.logger.warning(msg='create form skill')
        return super(SkillView, self).create_form(obj)

    def edit_form(self, obj=None):
        from wsgi import app
        app.logger.warning(msg='edit form skill')
        return super(SkillView, self).edit_form(obj)

    def is_accessible(self):
        from wsgi import app
        app.logger.warning(msg='authenticated user')
        return current_user.is_authenticated