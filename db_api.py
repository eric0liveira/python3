import MySQLdb

db = MySQLdb.connect(user="root", passwd="root", host="localhost", port=3306, db="db")
cursor = db.cursor()
cursor.execute()
print("Ok...")