import sys
import os as os
import datetime

def log(string):
	'''path = os.path.dirname(os.path.realpath(__file__)) + os.sep
	logToOldPath("1. Trying to log to new dir: + " + str(path))
	if str(path).contains("\\"):
		logToOldPath("2. Trying to log to new dir: + " + str(path))
		path = "\\".join(str(path).split("\\")[:-1]) # remove characters after last "/"" in filepath
		logToOldPath("3. Trying to log to new dir: + " + str(path))
	else:
		logToOldPath("4. Trying to log to new dir: + " + str(path))
		path = "/".join(str(path).split("/")[:-1]) # remove characters after last "/"" in filepath
		logToOldPath("5. Trying to log to new dir: + " + str(path))
	target = open(path + 'workoutapp_log.txt', 'a')		
	target.write("\n\n" + str(datetime.datetime.now()) + ": " + str(string) + "\n\n")
	target.close()
	'''
	return


def logToOldPath(string):
	'''
	target = open('workoutapp_log_old.txt', 'a')
	target.write("\n" + str(datetime.datetime.now()) + ": " + str(string) + "\n\n")
	target.write("Current dir is: " + str(os.path.dirname(os.path.realpath(__file__))))
	target.close()

	## ============
	#target = open('C:\\Program Files (x86)MacEwan Workout\workoutapp_log_new.txt', 'a')
	target = open(os.path.join("C:", "Users", "Chase", "workout_newtry.txt"), 'a')
	target.write("\n" + str(datetime.datetime.now()) + ": " + str(string) + "\n\n")
	target.write("Current dir is: " + str(os.path.dirname(os.path.realpath(__file__))))

	
	target.close()

	'''
	return