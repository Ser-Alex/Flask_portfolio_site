from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from werkzeug.security import generate_password_hash


class UserView(ModelView):
    """
    View model class skill for the admin panel
    """
    can_delete = False
    can_edit = True
    can_create = False

    create_modal = True
    edit_modal = True


    def on_model_change(self, view, model, is_created):
        """
        saving password as hash
        """
        from wsgi import app
        app.logger.warning(msg='generate hash password')
        model.password = generate_password_hash(model.password)

    def is_accessible(self):
        """
        user authentication
        """
        from wsgi import app
        app.logger.warning(msg='authenticated user')
        return current_user.is_authenticated