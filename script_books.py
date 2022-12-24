import sqlite3
import json
import os


file = "books.json"
p = "0"

conn = sqlite3.connect("flsite.db")
cur = conn.cursor()

pa = os.getcwd()

try:

	with open("books.json", encoding="utf8") as data_file:
		CONFIG_PROPERTIES = json.load(data_file)
except IOError as e:
	print(e)
	print("Error: can not open the file")

cont = CONFIG_PROPERTIES

#print(CONFIG_PROPERTIES['countries'][1])
print(cont)

for book in cont:
	cur.execute('INSERT INTO books VALUES (?, ?, ?, NULL)', (book['id'], book['book'], book['photo'],))
conn.commit()
conn.close()



