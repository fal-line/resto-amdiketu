import sqlite3
from sqlite3 import Error
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(THIS_FOLDER, 'resto.db')

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def create_crew(conn, crew):
    """
    Create a new crew into the crews table
    :param conn:
    :param crew:
    :return: crew id
    """
    sql = ''' INSERT INTO crew(nim,name)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, crew)
    conn.commit()
    return cur.lastrowid
        
def create_menu(conn, menu):
    """
    Create a new menu into the menus table
    :param conn:
    :param menu:
    :return: menu id
    """
    sql = ''' INSERT INTO menu(name,price)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, menu)
    conn.commit()
    return cur.lastrowid
        
def create_transaction(conn, transaction):
    """
    Create a new transaction into the transactions table
    :param conn:
    :param transaction:
    :return: transaction id
    """
    sql = ''' INSERT INTO transaction(crewName,date,totalMenu,totalPrice)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, transaction)
    conn.commit()
    return cur.lastrowid

def main():
    
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(THIS_FOLDER, 'resto.db')
    database = db_file

    sql_create_crew_table = """ CREATE TABLE IF NOT EXISTS crew (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        nim text NOT NULL,
                                        name text NOT NULL
                                    ); """

    sql_create_menu_table = """CREATE TABLE IF NOT EXISTS menu (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name text NOT NULL,
                                    price INTEGER NOT NULL
                                );"""

    sql_create_transaksi_table = """CREATE TABLE IF NOT EXISTS transaksi (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    crewName text NOT NULL,
                                    date text NOT NULL,
                                    totalMenu text NOT NULL,
                                    totalPrice INTEGER NOT NULL
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        print('Running...')
        
        #--------- CLEAN or FIRST TIME RUN ---------------------------------------
        create_table(conn, sql_create_crew_table) # create crew table
        create_table(conn, sql_create_menu_table) # create menu table
        create_table(conn, sql_create_transaksi_table) # create transaksi table
        
        crew = ('19221493','Muhammad Naufal Ihza Fadhilah');
        create_crew(conn, crew)
        crew = ('19220693','Aziz Ahadrianto');
        create_crew(conn, crew)
        crew = ('19220768','Alfa Rizy');
        create_crew(conn, crew)
        crew = ('19220682','M Bevi Arianda Anwar');
        create_crew(conn, crew)
        crew = ('19220458','M Zulfikar Noor');
        create_crew(conn, crew)
        crew = ('19220788','Dede saefulloh');
        create_crew(conn, crew)
        
        menu = ('Ayam Goweng','12000')
        create_menu(conn, menu)
        menu = ('My Ayayam','10000')
        create_menu(conn, menu)
        menu = ('Ayam Byakar','18000')
        create_menu(conn, menu)
        menu = ('Soto My Bogay','16000')
        create_menu(conn, menu)
        
    else:
        print("Error! database connection is not established.")

if __name__ == '__main__':
    main()