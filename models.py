"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Cupcake (db.Model):
    """ Cupcakes """

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    flavor = db.Column(db.Text, nullable = False)
    size = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Float, nullable = False)
    image = db.Column(db.Text, nullable = False, default='https://static.vecteezy.com/system/resources/previews/016/074/760/original/outline-simple-cupcake-icon-isolated-on-white-background-vector.jpg')

    def serialize(self):
        return {
            'id' : self.id,
            'flavor' : self.flavor,
            'size' : self.size,
            'rating' : self.rating,
            'image' : self.image
        }

    def __repr__(self):
        return f"<Cupcake {self.id} flavor={self.flavor} size={self.size}, rating={self.rating}"