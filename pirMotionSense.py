#/usr/bin/Python3
#Title: pirTest3.py
#Author: Bardic Knowledge
#Version: 0.2a
# Added timestamping to logging, and an exception handler for keyboard interrupts

import RPi.GPIO as GPIO
import time
from datetime import datetime
import logging

GPIO.setmode(GPIO.BOARD)
pir = 26
GPIO.setup(pir, GPIO.IN)

logging.basicConfig(level=logging.DEBUG, filename='example.log', filemode='a', format='%(asctime)s\tPIR SENSOR\t%(levelname)s\t%(message)s')
def logEntry (message, level="INFO"):
	timeNow = datetime.now()
	print ("{0}\tPIR SENSOR\t{1}\t{2}".format(str(timeNow), level, message))
def logInfo(message):
	logEntry(message, level="INFO")
	logging.info(message)

def logWarn(message):
	logEntry(message, level="WARN")
	logging.warning(message)

def logError(message):
	logEntry(message, level="ERROR")
	logging.error(message)

time.sleep(2) # initialize PIR Motion Sensor

logWarn("Detecting motion")
while True:
	try:
		if GPIO.input(pir):
			logWarn("Motion Detected!")
			while GPIO.input(pir):
				time.sleep(1)
			logWarn("Motion Detection Ended!")
		time.sleep(0.1)
	except KeyboardInterrupt:
		logError("Keyboard Interrupt!")
		break
