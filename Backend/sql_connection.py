import mysql.connector

__cnx = None


def get_sql_connection():
    """
    get_sql_connection _summary_

    _extended_summary_
    """
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(
            user="root",
            password="Damilola@2007.",
            host="127.0.0.1",
            port="1000",
            database="gs",
        )

    return __cnx
