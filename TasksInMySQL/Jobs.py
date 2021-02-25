from DatabaseContextManager import DatabaseContextManager


def create_table_jobs():
    query = """CREATE TABLE `jobs`(
    `id` integer NOT NULL AUTO_INCREMENT,
    `company_id` integer,
    `category_id` integer,
    `job_title` varchar(255),
    `salary` DECIMAL(50, 2),
    `description` varchar(255),
    `location` varchar(100),
    `position` varchar(100),
    `category` varchar(100),
    PRIMARY KEY (id),
    FOREIGN KEY (company_id) REFERENCES companies(id),
    FOREIGN KEY (category_id) REFERENCES categories(id));"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)


def create_jobs(company_id, category_id, job_title, salary, description, location, position, category):
    query = """INSERT INTO jobs
                (company_id, category_id, job_title, salary, description, location, position, category)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    """
    parameters = [company_id, category_id, job_title, salary, description, location, position, category]
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query, parameters)


def get_jobs():
    query = """SELECT * FROM jobs"""
    with DatabaseContextManager() as db:
        cursor = db.cursor()
        cursor.execute(query)
        print(cursor.fetchall())


def delete_jobs(job_id):
    query = """DELETE FROM jobs
                WHERE id = ?"""
    parameters = [job_id]
    with DatabaseContextManager() as db:
        db.execute(query, parameters)


def get_all_tables():
    query = """SELECT * FROM jobs
                NATURAL JOIN companies """
    with DatabaseContextManager(is_select=True) as db:
        cursor = db.cursor()
        cursor.execute(query)
        print(cursor.fetchall())
