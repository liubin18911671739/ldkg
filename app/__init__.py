from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from app.database.neo4j_client import Neo4jClient
from app.chatgpt.chatgpt_client import ChatGPTClient

bootstrap = Bootstrap()
neo4j_client = Neo4jClient()
chatgpt_client = ChatGPTClient()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    bootstrap.init_app(app)
    neo4j_client.init_app(app)
    chatgpt_client.init_app(app)

    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app