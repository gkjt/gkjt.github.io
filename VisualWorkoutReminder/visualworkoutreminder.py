import time
import datetime
import cmd
import subprocess
import os
import random

run = True



#using http://www.sirentuan.com/3780124/codep1/python-open-pdf-file-to-specific-pagesection
def openWorkout():
	path_to_pdf = os.path.abspath('.\100-no-equipment-workouts-2014-by-neilarey.pdf')
	path_to_acrobat = os.path.abspath('C:\Program Files (x86)\Adobe\Reader 10.0\Reader\AcroRd32.exe') 
	
	page = random.randrange(10, 100, 2)
	
	process = subprocess.Popen([path_to_acrobat, '/A', 'page=' + str(page), path_to_pdf], shell=False, stdout=subprocess.PIPE)
	process.wait()


while run:
	now = datetime.datetime.today()
	nextWorkout = now #datetime.datetime(now.year, now.month, now.day, 19, 22)
	#if(now.hour >= 16):
		#nextWorkout += datetime.timedelta(days=0)
	print((nextWorkout-now).seconds)
	time.sleep((nextWorkout-now).seconds)
	openWorkout()
	#DEBUG:
	run = False
	
