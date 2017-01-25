import sqlite3

from Person import Person

# Generate a createTable string by getting the attributes from peron
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

def getInsertPersonString(person):
	statement = list()
	attribList = Person().getAttributes()
	statement.append("INSERT INTO PEOPLE (")
	for i in attribList:
		statement.append(i)
		statement.append(",")
	del statement[len(statement)-1]

	statement.append(") VALUES (")
	for i in attribList:
		statement.append('\'')
		statement.append(getattr(person, i))
		statement.append('\'')
		statement.append(",")
	del statement[len(statement)-1]
	statement.append(")")
	return "".join(statement)

def createDB():
	conn = sqlite3.connect('people.db')
	print("Opened database successfully")
	conn.execute(getCreateTableString())
	print("Table created successfully")
	conn.close()


def insertPerson(person):
	conn = sqlite3.connect('people.db')
	#conn.execute("INSERT INTO PEOPLE (ID,NAME,PHONE,DATEOFTEST,GENDER,DOB,HEARTRATE,BLOODPRESSURE,HEIGHT,WEIGHT) VALUES (1, 'Paul', '780-700-1070', testDate, 'male',dob, 100, 200, 300, 400)")
	conn.execute(getInsertPersonString(person))
	conn.commit()
	conn.close()

def getPeople():
	people = list()
	conn = sqlite3.connect('people.db')
	cursor = conn.execute("SELECT * from PEOPLE")
	
	for row in cursor:
		people.append(loadPersonFromDBSelect(row))

	conn.close()
	return people

def loadPersonFromDBSelect(dbSelect):
	p = Person()
	attribList = p.getAttributes()
	# skip the database ID
	for i in range(1,len(dbSelect)):
		setattr(p, attribList[i-1], dbSelect[i])
	return p

def testDBStuff():
	p = Person()
	p.name = "John"
	p.armcirc = "10"
	p.plantTime = "100"
	p.weight = "5"
	p.RMPredictEx = "rm stuff"
	insertPerson(p)

	r = getPeople()[0]

	assert(r.name == p.name)
	assert(r.armCirc == p.armCirc)
	assert(r.weight == p.weight)
	assert(r.height == p.height)
