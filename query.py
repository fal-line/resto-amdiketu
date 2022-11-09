import sqlite3
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(THIS_FOLDER, 'resto.db')
print(db_file)

# Create a SQL connection to our SQLite database
con = sqlite3.connect(db_file)
cur = con.cursor()

crewRaw = []
crewData = []
crewID = []
crewName =[]


# def crewRaw(cur,crewData,crewID,crewName):
#     cur.execute('SELECT * FROM crew;')
#     row = cur.fetchall()
#     for row in row:
#         crewData.append(row)
#         crewID.append(row[1])
#         crewName.append(row[2])
#     return crewData, crewID, crewName

# crewRaw(cur,crewData,crewID,crewName)
class crewRaw():
    def data(crewData):
        cur.execute('SELECT * FROM crew;')
        row = cur.fetchall()
        for row in row:
            crewData.append(row)
        return crewData
    
    def id(crewID):
        cur.execute('SELECT nim FROM crew;')
        row = cur.fetchall()
        for row in row:
            crewID.append(row)
        return crewID
    
    def name(crewName):
        cur.execute('SELECT name FROM crew;')
        row = cur.fetchall()
        for row in row:
            crewName.append(row)
        return crewName

print(crewRaw.id(crewData))
# key = '19220682'
# for a in a:
#     if key in a[1]:
#         print('User tedaftar dengan NIM',a[1],'dan dengan nama',a[2])
#         continue

    


# def menuList(cur,row,menuFull):
#     cur.execute('SELECT * FROM menu;')
#     row = cur.fetchall()
#     for row in row:
#         menuFull.append(row)
#     return menuFull
    


    

# Be sure to close the connection
# con.close()