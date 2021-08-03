"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):

    __tablename__ = "cupcakes"

    id = db.Column(db.Integer,primary_key=True,autoincrement = True)

    flavor = db.Column(db.String(50),nullable = False)

    size = db.Column(db.String(50),nullable = False)

    rating = db.Column(db.Float,nullable = False)

    image = db.Column(db.String(200),default="https://tinyurl.com/demo-cupcake",nullable = False)


