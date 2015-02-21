import time
import datetime
import cmd
import webbrowser
import os
import random

run = True



#using http://www.sirentuan.com/3780124/codep1/python-open-pdf-file-to-specific-pagesection
def openWorkout():
	path_to_site = "http://neilarey.com/workouts.html"
	webbrowser.open(path_to_site, new=0, autoraise=True)
	

while run:
	now = datetime.datetime.today()
	nextWorkout = datetime.datetime(now.year, now.month, now.day, 16, 30)
	if(now >= nextWorkout):
		nextWorkout += datetime.timedelta(days=1)
	print((nextWorkout-now).seconds)
	time.sleep((nextWorkout-now).seconds)
	openWorkout()
	#DEBUG:
	run = False
	
