import time
import datetime
import cmd
import subprocess
import os
import random

run = true


//using http://www.sirentuan.com/3780124/codep1/python-open-pdf-file-to-specific-pagesection
def openWorkout()
	path_to_pdf = os.path.abspath('.\100-no-equipment-workouts-2014-by-neilarey.pdf')
	path_to_acrobat = os.path.abspath('C:\Program Files (x86)\Adobe\Reader 10.0\Reader\AcroRd32.exe') 
	
	page = random.randint(10, 100, 2)
	
	process = subprocess.Popen([path_to_acrobat, '/A', 'page=' + page, path_to_pdf], shell=False, stdout=subprocess.PIPE)
	process.wait()


while run:
	now = datetime.datetime.today()
	nextWorkout = datetime.datetime(t.year,t.month,t.day,16,30)
	if(now.hour >= 16)
		nextWorkout += time.timeDelta(days=1)
	time.sleep((nextWorkout-now).seconds)
	openWorkout()
	//DEBUG:
	run = false
