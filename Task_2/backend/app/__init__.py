from flask import Flask

from .config import Config
from .extensions import cache, cors, db
from .routes.tasks import bp as tasks_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    cache.init_app(app)

    # Build CORS origins list
    fe_host = app.config["FE_HOST"]
    cors_origins = [f"http://{fe_host}", f"https://{fe_host}"]

    cors.init_app(
        app,
        resources={
            r"/api/tasks*": {
                "origins": cors_origins,
                "allow_headers": "*",
                "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            }
        },
    )

    # Register blueprints
    app.register_blueprint(tasks_bp)

    # Debug: print all routes
    with app.app_context():
        for rule in app.url_map.iter_rules():
            print(f"Route: {rule.rule} -> {rule.endpoint}")

    return app
