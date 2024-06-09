import mysql.connector

from config import HOST, USER, PASSWORD


class DBConnectionError(Exception):
    pass


def _connect_to_db(db_name: str):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return connection


def find_substitution(sub_ingredient):
    try:
        db_name = "SUBSTITUTIONS"
        db_connection = _connect_to_db(db_name)
        cursor = db_connection.cursor()
        substituiton_search = """SELECT
    fi.Food_Name AS Original_Ingredient,
    fa.Food_Name AS Alternative_Ingredient
FROM
    Alternatives a
JOIN
    FoodItems fi ON a.Food_ID = fi.Food_ID
JOIN
    FoodItems fa ON a.Alternative_Food_ID = fa.Food_ID
WHERE
	fi.Food_Name = '{}';""".format(sub_ingredient)
        cursor.execute(substituiton_search)
        results = cursor.fetchall()
        cursor.close()
        return results
    except Exception:
        raise DBConnectionError("Failed to Connection to the DB")
