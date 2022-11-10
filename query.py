import sqlite3
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(THIS_FOLDER, 'resto.db')
# print(db_file)

# Create a SQL connection to our SQLite database
con = sqlite3.connect(db_file)
cur = con.cursor()

getData = []
crewData = []
menuData = []
strukData = []
dic = {}

class getData():
    def crew(crewData):
        cur.execute('SELECT * FROM crew;')
        row = cur.fetchall()
        for row in row:
            dic['id'] = row[0]
            dic['nim'] = row[1]
            dic['name'] = row[2]
            crewData.append(dic.copy())
        return crewData
    
    def menu(menuData):
        cur.execute('SELECT * FROM menu;')
        row = cur.fetchall()
        for row in row:
            dic['id'] = row[0]
            dic['name'] = row[1]
            dic['price'] = row[2]
            menuData.append(dic.copy())
        return menuData
    
    def struk(strukData):
        cur.execute('SELECT * FROM transaksi;')
        row = cur.fetchall()
        for row in row:
            dic['id'] = row[0]
            dic['crewName'] = row[1]
            dic['date'] = row[2]
            dic['totalMenu'] = row[3]
            dic['totalPrice'] = row[4]
            strukData.append(dic.copy())
        return strukData
