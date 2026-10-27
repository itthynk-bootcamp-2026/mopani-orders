import sqlite3


def get_connection(path="shop.db"):
    return sqlite3.connect(path)


def setup(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    conn.executemany(
        "INSERT INTO customers (name, email) VALUES (?, ?)",
        [("Thandi", "thandi@example.com"), ("Pieter", "pieter@example.com")],
    )
    conn.commit()


def find_customer(conn, name):
    # Look up a customer by name
    query = "SELECT id, name, email FROM customers WHERE name = '" + name + "'"
    return conn.execute(query).fetchall()
