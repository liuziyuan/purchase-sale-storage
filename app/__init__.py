from app.routes import api

class App(object):
    def __init__(self, app=None):
        self.app = None
        if app is not None:
            self.app = app
            self.init_app(app)

    def init_app(self, app):
        api.init_app(app)

