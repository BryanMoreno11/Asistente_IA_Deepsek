from flask import Flask
from flask_cors import CORS
from backend.routes.asistant_routes import bp_rag


def create_app():
    app = Flask(__name__)
    #Configurar Cors
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # Registrar blueprints
    app.register_blueprint(bp_rag, url_prefix="/api")
    return app
