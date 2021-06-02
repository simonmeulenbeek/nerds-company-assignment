import os
from flask import Flask

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='abc123',
        DATABASE='db.sqlite'
    )

    if config is not None:
        app.config.from_mapping(config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def home():
        return 'home!'
    
    from . import db
    db.connect_app(app)
    
    from . import authorize
    app.register_blueprint(authorize.blueprint)

    from . import login
    app.register_blueprint(login.blueprint)
    
    return app