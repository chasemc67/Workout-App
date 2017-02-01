import sqlite3

from Person import Person

# Generate a createTable string by getting the attributes from peron
def getCreateTableString():
	statement = list()
	statement.append("CREATE TABLE IF NOT EXISTS\nPEOPLE(\nID INTEGER PRIMARY KEY AUTOINCREMENT")

	attribList = Person().getAttributes()
	for i in attribList:
		statement.append(",\n" + i)

		# set db type depending on attrib
		if i.lower() == "frameschecked":
			statement.append(" CHAR(1000)")
		else:
			statement.append(" CHAR(50)")

		if i.lower() == "name":
			statement.append(" NOT NULL")
	statement.append(");")

	return "".join(statement)

# Takes a person object and generates a string to insert
# that person object into the DB
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

		# get list of framesChecked as a string if 
		# thats the attribute we're adding
		if i.lower() == "frameschecked":
			statement.append('\'')
			statement.append(person.getFramesCheckedString())
			statement.append('\'')
			statement.append(",")
		else:
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

# Takes a person object and inserts it into the DB
def insertPerson(person):
	conn = sqlite3.connect('people.db')
	if person.name.strip() == "":
		raise Exception("Tried to save person with no name to DB")
	conn.execute(getInsertPersonString(person))
	conn.commit()
	conn.close()

	print("inserted new person: " + str(person.name))

# Returns a list of all people object in DB
def getPeople():
	people = list()
	conn = sqlite3.connect('people.db')
	cursor = conn.execute("SELECT * from PEOPLE")
	
	for row in cursor:
		people.append(loadPersonFromDBSelect(row))

	conn.close()
	return people

# Helper function for getPeople function
def loadPersonFromDBSelect(dbSelect):
	p = Person()
	attribList = p.getAttributes()
	# skip the database ID
	for i in range(1,len(dbSelect)):
		# set attriv differently if its the framesChecked string
		if attribList[i-1].lower() == "frameschecked":
			p.setFramesCheckedList(dbSelect[i])
		else: 
			setattr(p, attribList[i-1], dbSelect[i])
	p.dbID = dbSelect[0]
	return p


def insertTestPeople():
	p = Person()
	p.name = "Bill"
	p.armcirc = "10"
	p.plantTime = "100"
	p.weight = "5"
	p.RMPredictEx = "rm stuff"
	insertPerson(p)

	p = Person()
	p.name = "Chase"
	p.armcirc = "10"
	p.plantTime = "100"
	p.weight = "5"
	p.RMPredictEx = "rm stuff"
	insertPerson(p)

	p = Person()
	p.name = "Megan"
	p.armcirc = "10"
	p.plantTime = "100"
	p.weight = "5"
	p.RMPredictEx = "rm stuff"
	insertPerson(p)

# Test function for testing DB
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
