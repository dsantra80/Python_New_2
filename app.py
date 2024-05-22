from flask import Flask
from routes import main_blueprint
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    app.register_blueprint(main_blueprint)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
    