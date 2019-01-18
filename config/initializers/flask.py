from flask import Flask
import os
import yaml
from flask_environments import Environments

class EnvironmentsExtended(Environments):
    def from_yaml(self, path):
        with open(path) as f:
            c = yaml.load(f)

        for name in self._possible_names():
            try:
                c = c[name]
            except:
                pass

        app = self.get_app()

        for key in c.keys():
            if key.isupper():
                app.config[key] = c[key]
    

app = Flask(__name__)
env = EnvironmentsExtended(app)
env.from_yaml(os.path.join(os.getcwd(), 'config', 'config.yml'))
