import sqlite3

from Person import Person

def getCreateTableString():
	statement = list()
	statement.append("CREATE TABLE IF NOT EXISTS\nPEOPLE(\nID INTEGER PRIMARY KEY AUTOINCREMENT")

	attribList = Person().getAttributes()
	for i in attribList:
		statement.append(",\n" + i + " CHAR(50)")
		if i.lower() == "name":
			statement.append(" NOT NULL")
	statement.append(");")

	return "".join(statement)

def createDB():
	conn = sqlite3.connect('people.db')
	print("Opened database successfully")


	conn.execute(getCreateTableString())

	print("Table created successfully")

	conn.close()