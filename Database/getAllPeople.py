import sqlite3

def getAllPeople():
	conn = sqlite3.connect('people.db')
	cursor = conn.execute("SELECT * from PEOPLE")
	for row in cursor:
		print ("ID = " + str(row[0]))
		print ("NAME = " + str(row[1]))
		print ("PHONE = " + str(row[2]))
		print ("DATEOFTEST = " + str(row[3]))		
		print ("GENDER = " + str(row[4]))
		print ("DOB = " + str(row[5]))
		print ("HEARTRATE = " + str(row[6]))
		print ("BLOODP = " + str(row[7]))
		print ("HEIGHT = " + str(row[8]))
		print ("WEIGHT = " + str(row[9]) + "\n") 