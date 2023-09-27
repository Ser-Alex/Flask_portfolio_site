from flask import redirect, url_for, request
from flask_admin import AdminIndexView, expose, helpers
from flask_login import current_user, login_user, logout_user

from portfolioapp.admin.form import LoginForm


class MyAdminIndexView(AdminIndexView):
    """
    Class admin panel
    """
    @expose('/')
    def index(self):
        """
        page index function: checks user authorization

        :return: depending on the user's authorization, it is sent to different pages
        """
        from wsgi import app
        app.logger.info(msg='get started with "admin_index" functions')

        if not current_user.is_authenticated:
            app.logger.info(msg='User is not authenticated redirect login_view')
            return redirect(url_for('.login_view'))

        app.logger.info(msg='User is authenticated return page')
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        """
        page function /login for user authorization

        :return: depending on the result, the user sends inputs to the index page or logs in again
        """
        from wsgi import app
        app.logger.info(msg='get started with "login_index" functions')

        form = LoginForm(request.form)
        app.logger.info(msg='loading a form from a page')

        if helpers.validate_form_on_submit(form):
            app.logger.info(msg='the form is valid')

            user = form.get_user()
            app.logger.info(msg='loaded user from the form')

            login_user(user)
            app.logger.debug(msg='User authenticated')

        if current_user.is_authenticated:
            app.logger.info(msg='User is authorized I return to the index page')
            return redirect(url_for('.index'))

        self._template_args['form'] = form
        app.logger.info(msg='I return the login page with the completed form')
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        """
        logout function

        :return: redirects to the index page
        """
        from wsgi import app
        app.logger.info(msg='get started with "logout_index" functions')

        logout_user()
        app.logger.debug(msg='User is logout, redirect index page')
        return redirect(url_for('.index'))