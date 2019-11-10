import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_values(conn, data):
    sql = """ INSERT INTO users(name, email, balance)
        VALUES(?, ?, ?)"""
    cur = conn.cursor()
    cur.execute(sql, data)
    return cur.lastrowid

def main():
    database = r"D:/sqlite/db/pythonsqlite.db"
    conn = create_connection(database)

    # sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users(
    #     name text NOT NULL,
    #     email text NOT NULL,
    #     balance integer
    # );"""

    # if conn is not None:
    #     create_table(conn, sql_create_users_table)
    #     print('created table')
    # else:
    #     print("Error! Can not create the database connection...")

    with conn:
        user_1_data = ('a', 'a@a.com', 20)
        user_2_data = ('b', 'b@b.com', -5)

        insert_values(conn, user_1_data)
        insert_values(conn, user_2_data)

if __name__ == '__main__':
    main()
