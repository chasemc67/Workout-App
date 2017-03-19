import sys
#import os as os
import datetime

def log(string):
	#path = os.path.dirname(os.path.realpath(__file__))
	#ath = "/".join(path.split("/")[:-1]) # remove characters after last "/"" in filepath
	#target = open(path + '/workoutapp_log.txt', 'a')
	#target.write("\n\n" + str(datetime.datetime.now()) + ": " + str(string) + "\n\n")
	#target.close()
	print()


def logToOldPath(string):
	target = open('workoutapp_log_old.txt', 'a')
	target.write("\n" + str(datetime.datetime.now()) + ": " + str(string) + "\n\n")
	target.close()