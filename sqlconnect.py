import sqlite3


def connection(dbname):
    conn = sqlite3.connect(dbname)
    # creating table
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTEL (NAME TEXT, ADDRESS TEXT, RATING INT, PRICES INT,AMENITIES TEXT)")
    conn.close()


def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    conn.execute("INSERT INTO OYO_HOTEL (NAME, ADDRESS, RATING, PRICES, AMENITIES) VALUES (?, ?, ?, ?, ?)",values)
    conn.commit()
    conn.close()


def display_table(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    data = cur.fetchall()

    cur.execute("SELECT * FROM OYO_HOTEL")
    for record in data:
        print(record)

    conn.close()