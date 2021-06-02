import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def home():
        return 'home!'

    from . import db
    db.connect_app(app)
    
    return app