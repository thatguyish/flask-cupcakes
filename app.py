"""Flask app for Cupcakes"""
from flask import Flask, json, jsonify, request
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

@app.route('/api/cupcakes')
def get_all_cupcakes():
    all_cupcakes = Cupcake.query.all()
    cupcakes = [cupcake.serialize() for cupcake in all_cupcakes]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes',methods=["POST"])
def add_cupcake():
    cupcake = Cupcake(flavor=request.json['flavor'],size=request.json['size'],rating=request.json['rating'],image=request.json['image'],)
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize()), 201

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>',methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)

    cupcake.flavor = request.json.get('flavor',cupcake.flavor)
    cupcake.image = request.json.get('image',cupcake.image)
    cupcake.rating = request.json.get('rating',cupcake.rating)
    cupcake.size = request.json.get('size',cupcake.size)

    db.session.add(cupcake)
    db.session.commit()

    return cupcake.serialize()

@app.route('/api/cupcakes/<int:id>',methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return {"message":"Deleted"}
