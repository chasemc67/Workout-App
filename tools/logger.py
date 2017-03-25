import sys
import os as os
import datetime

def log(string):
	if not os.path.exists('Workout_App_Data'):
		os.makedirs('Workout_App_Data')

	target = open('Workout_App_Data\workoutapp_log.txt', 'a')
	target.write("\n" + str(datetime.datetime.now()) + ": " + str(string) + "\n\n")
	#target.write("Current dir is: " + str(os.path.dirname(os.path.realpath(__file__))))
	target.close()
