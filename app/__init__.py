from flask import Flask
from app.routes.home import home_bp
from app.routes.student import student_bp
from app.routes.instructor import instructor_bp
from app.routes.program import program_bp
from app.routes.license import license_bp
from app.routes.aiu import aiu_bp
from app.routes.coursera import coursera_bp
from app.routes.coordinator import coordinator_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(coordinator_bp)
    app.register_blueprint(instructor_bp)
    app.register_blueprint(program_bp)
    app.register_blueprint(license_bp)
    app.register_blueprint(aiu_bp)
    app.register_blueprint(coursera_bp)

    return app
