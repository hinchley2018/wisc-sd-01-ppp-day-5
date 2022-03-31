from flask import Flask, request, render_template
from . import pets
# app factory
def create_app():
    #create app
    app = Flask(__name__)

    #config -> wire up your other routes

    @app.route('/')
    def index():
        return render_template(
            'index.html',
            nav_items=[
                {
                    'path': '/pets',
                    'name': 'Pets'
                },
                {
                    'path': '/pets/create-pets',
                    'name': 'Create Pets'
                }
            ]
        )

    #make sure it is inside the fucntion before the app instance is returned
    app.register_blueprint(pets.pets_bp)
    
    return app

