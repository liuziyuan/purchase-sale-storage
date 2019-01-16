from app.router import api


class App(object):
    """
    The main entry point for the application.
    You need to initialize it with a Flask Application::
    Examples::
            my_app = App()
            api.init_app(app)
    Or::
            App(app)        
    """
    def __init__(self, app=None):
        self.app = None
        if app is not None:
            self.app = app
            self.init_app(app)

    def init_app(self, app):
        api.init_app(app)

