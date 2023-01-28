from flask import Flask, request, jsonify
import products_dao
from sql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()


@app.route("/getProducts", methods=["GET"])
def get_products():
    """
    get_products _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/deleteProducts", methods=["POST"])
def delete_product():
    """
    delete_product _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
    return_id = products_dao.delete_product(connection, request.form["product_id"])
    response = jsonify({"product_id": return_id})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    print(
        "Starting Python Flask Server on Port:5000 For Grocery Store Management System "
    )
    app.run(port=5000)
