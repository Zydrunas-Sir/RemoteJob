from DatabaseContextManager import DatabaseContextManager


def create_table_categories():
    query = """CREATE TABLE `categories`(
    id integer NOT NULL AUTO_INCREMENT,
    name varchar(255),
    PRIMARY KEY (id));"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)


def create_categories(name):
    query = """INSERT INTO categories(name) VALUES(%s)
    """
    parameters = [name]
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query, parameters)


def get_categories():
    query = """SELECT * FROM categories"""
    with DatabaseContextManager("db") as db:
        cursor = db.cursor()
        cursor.execute(query)


def delete_categories(category_id):
    query = """DELETE FROM categories
                WHERE id = ?"""
    parameters = [category_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
