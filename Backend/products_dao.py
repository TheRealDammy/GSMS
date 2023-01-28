"""
     _summary_

    _extended_summary_
"""
from sql_connection import get_sql_connection


def get_all_products(connection):
    """
    get_all_products This gets all the products listed un the database
    """

    cursor = connection.cursor()
    query = (
        " SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
        "FROM gs.products inner join uom on products.uom_id=uom.uom_id"
    )
    cursor.execute(query)

    response = []

    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                "product_id": product_id,
                "name": name,
                "uom_id": uom_id,
                "price_per_unit": price_per_unit,
                "uom_name": uom_name,
            }
        )

    return response


def insert_new_product(connection, products):
    """
    A function to all the users insert their own products into the database

    Args:
        connection (_type_): This specifies the connection
        products (_type_): these are the products the user would like to enter

    return:
        This returns the Id of the last entry into the database

    """
    cursor = connection.cursor()
    query = " INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s,%s,%s)"
    data = (products["product_name"], products["uom_id"], products["price_per_unit"])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, product_id):
    """
    delete_product: This allows a user to delete a product already entered into the database

    Args:
        connection (_type_): This specifies the connection
        product_id (_type_): This is the ID of the Product
    """
    cursor = connection.cursor()
    query = " DELETE FROM products where product_id=" + str(product_id)
    cursor.execute(query)
    connection.commit()


if __name__ == "__main__":
    connection = get_sql_connection()
    print(delete_product(connection, 10))
