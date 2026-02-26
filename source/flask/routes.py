from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

@app.route("/auth/register", methods=["POST"])
def register():
    pass

@app.route("/auth/login", methods=["POST"])
def login():
    pass

@app.route("/auth/me", methods=["GET"])
@jwt_required()
def me():
    pass

@app.route("/categories", methods=["GET"])
def get_categories():
    pass

@app.route("/categories", methods=["POST"])
@jwt_required()
def create_category():
    pass

@app.route("/categories/<int:cat_id>", methods=["GET", "PUT", "DELETE"])
@jwt_required()
def category(cat_id):
    pass

@app.route("/products", methods=["GET"])
def get_products():
    pass

@app.route("/products", methods=["POST"])
@jwt_required()
def create_product():
    pass

@app.route("/products/<int:pid>", methods=["GET", "PUT", "DELETE"])
@jwt_required()
def product(pid):
    pass

@app.route("/products/my", methods=["GET"])
@jwt_required()
def my_products():
    pass

@app.route("/search", methods=["GET"])
def search():
    pass

if __name__ == "__main__":
    app.run(debug=True)