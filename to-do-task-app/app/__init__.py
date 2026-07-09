from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "0812"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  
    if os.environ.get('VERCEL'):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/todo.db'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    
    db.init_app(app)
   
    from app.routes.auth import auth_bp
    from app.routes.task import task_bp
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(task_bp, url_prefix='/tasks')

    

    @app.route('/')
    def index():
        return redirect(url_for('auth.register'))
    
    with app.app_context():
        db.create_all()

    return app