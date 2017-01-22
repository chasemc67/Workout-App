import sqlite3

def createDB():
	conn = sqlite3.connect('people.db')
	print("Opened database successfully")

	conn.execute('''CREATE TABLE IF NOT EXISTS
		PEOPLE (
	       ID INT PRIMARY KEY     NOT NULL,
	       NAME           CHAR(50)    NOT NULL,
	       PHONE          CHAR(50),
	       DATEOFTEST        CHAR(50),
	       GENDER			CHAR(10),
	       DOB				CHAR(50),
	       HEARTRATE		INT,
	       BLOODPRESSURE	INT,
	       HEIGHT			INT,
	       WEIGHT			INT
	    );''')

	print("Table created successfully")

	conn.close()