"""Web Server Gateway Interface"""

#pip install apispec apispec_webframeworks marshmallow

##################
# FOR PRODUCTION
####################
from src.app import app
from src.blueprints.db.models import db
from src.blueprints.db.models import login
from datetime import timedelta

if __name__ == "__main__":
    ####################
    # FOR DEVELOPMENT
    ####################

    # Для генерации секретного ключа
    # import os
    # os.urandom(50)
    # app.config['SECRET_KEY'] = ''
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=5)

    db.init_app(app)
    login.init_app(app)
    login.login_view = 'login.auth'

    @app.before_first_request
    def create_all():
        db.create_all()

    app.run(host='0.0.0.0', debug=True)