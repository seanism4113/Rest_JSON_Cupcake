"""Flask app for Cupcakes"""
from flask import Flask, jsonify, request, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret-recipe"

connect_db(app)
app.app_context().push()

@app.route('/')
def homepage():
    """ Render homepage which will have a list of cupcakes and form to add new cupcakes"""
    return render_template('index.html')

@app.route('/api/cupcakes')
def list_cupcakes():
    """ Return all cupcakes in api"""
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = cupcakes)

@ app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """ retrieve and return data for single cupcake from api"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """ create new cupcake to add to api and return data about new cupcake"""
    new_cupcake = Cupcake(flavor = request.json['flavor'],
                          size = request.json['size'],
                          rating = request.json['rating'],
                          image = request.json['image'] or None)
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake = new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """ Update one or more fields in a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """ Delete a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message = 'Deleted!')
