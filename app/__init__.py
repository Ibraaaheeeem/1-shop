import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Initialize SQLAlchemy and Migrate instances without app context
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    
    app = Flask(__name__)

    # Configure database URL from environment variable
    database_url = os.environ.get('1SHOP_DB')

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pass@localhost:5432/oneshop"

    # Configure secret key for jwt
    secret_key = os.environ.get('JWT_KEY')
    app.config['JWT_SECRET_KEY'] = secret_key

    # Initialize db and migrate with the app
    db.init_app(app)
    migrate.init_app(app, db)
    #jwt.init_app(app)

    from .routes.categories import categories_bp
    from .routes.properties import properties_bp
    from .routes.products import products_bp

    app.register_blueprint(categories_bp, url_prefix='/categories')
    app.register_blueprint(properties_bp, url_prefix='/properties')
    app.register_blueprint(products_bp, url_prefix='/products')
    return app