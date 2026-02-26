from flask import Flask, jsonify
from source.selenium import elan_datasi

app = Flask(__name__)

@app.route("/auth/register", methods=["POST"])
def register():
    pass

@app.route("/auth/login", methods=["POST"])
def login():
    pass

@app.route("/auth/me", methods=["GET"])
def me():
    pass

@app.route("/categories", methods=["GET"])
def get_categories():
    pass

@app.route("/categories", methods=["POST"])
def create_category():
    pass

@app.route("/categories/<int:cat_id>", methods=["GET", "PUT", "DELETE"])
def category(cat_id):
    pass

@app.route("/products/<int:product_id>", methods=["GET"])
def get_products(product_id):
    data = elan_datasi(product_id)
    return jsonify(data)

@app.route("/products", methods=["POST"])
def create_product():
    pass

@app.route("/products/<int:pid>", methods=["GET", "PUT", "DELETE"])
def product(pid):
    pass

@app.route("/products/my", methods=["GET"])
def my_products():
    pass

@app.route("/search", methods=["GET"])
def search():
    pass

if __name__ == "__main__":
    app.run(debug=True)