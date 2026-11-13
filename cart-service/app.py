from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cart = []


@app.route("/")
def home():
    return "Cart Service Running"


@app.route("/add", methods=["POST"])
def add_item():

    item = request.form.get("item")

    cart.append(item)

    return jsonify(
    {
        "message":"Item added",
        "item":item
    })


@app.route("/remove", methods=["POST"])
def remove_item():

    item = request.form.get("item")

    if item in cart:

        cart.remove(item)

        return jsonify(
        {
            "message":"Removed one item"
        })

    return jsonify(
    {
        "message":"Item not found"
    })


@app.route("/delete", methods=["POST"])
def delete_item():

    item = request.form.get("item")

    while item in cart:

        cart.remove(item)

    return jsonify(
    {
        "message":"Deleted item"
    })


@app.route("/clear", methods=["POST"])
def clear_cart():

    cart.clear()

    return jsonify(
    {
        "message":"Cart cleared"
    })


@app.route("/cart", methods=["GET"])
def get_cart():

    return jsonify(cart)


app.run(
    host="0.0.0.0",
    port=5003
)
