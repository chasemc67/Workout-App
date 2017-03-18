import sys
import datetime

def log(string):
	target = open('workoutapp_log.txt', 'a')
	target.write("\n" + str(datetime.datetime.now()) + ": " + str(string) + "\n")
	target.close()

