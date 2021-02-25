from DatabaseContextManager import DatabaseContextManager


def create_table_companies():
    query = """CREATE TABLE `companies`(
    `id` integer NOT NULL AUTO_INCREMENT,
    `name` varchar(255),
    `description` varchar(255),
    `headquarters_location` varchar(255),
    `average_salary` DECIMAL(50, 2),
    PRIMARY KEY (id));"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)


def create_companies(name, description, headquarters_location, average_salary):
    query = """INSERT INTO companies(name, description, headquarters_location, average_salary) VALUES(%s, %s, %s, %s)
    """
    parameters = [name, description, headquarters_location, average_salary]
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query, parameters)


def get_companies():
    query = """SELECT * FROM companies"""
    with DatabaseContextManager("db") as db:
        cursor = db.cursor()
        cursor.execute(query)


def delete_companies(company_id):
    query = """DELETE FROM companies
                WHERE id = ?"""
    parameters = [company_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
