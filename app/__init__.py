from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from neo4j import GraphDatabase


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bootstrap = Bootstrap(app)

    with app.app_context():
        from main import bp as main_blueprint

        app.register_blueprint(main_blueprint)

    return app


app = create_app()
