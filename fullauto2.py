#!/usr/bin/python

import time
import serial
import requests
import os
import logging

ser = serial.Serial('/dev/ttyACM0', 9600)
logging.basicConfig(format='%(asctime)s:%(message)s', filename='/home/pi/cottage.log', filemode='w', level=logging.INFO)

start = {}
stop = {}
circ = {1: 'Main', 2: 'Water', 3: 'Bed'}
circn = {}
on = {}
off = {}
state = {}

def readSettings():
        "Read in settings from the file created by parsecal.py"
        f = open('/home/pi/cottage.txt')
	global lines
	lines = f.readlines()
	logging.info(lines)
	f.close

def testSer():
        "Confirm that serial communications are good, and start establish serial connection if necessary"
        global ser
        if ser.writable():
                logging.info('Serial communications are up.')
        else:
                logging.warning('Restarting serial communications')
                ser = serial.Serial('/dev/ttyACM0', 9600)
                time.sleep(2)

def sendSignal():
	"Create dictonary from cottage.txt, and write to arduino as appropriate"
	x=1
	global lines
	for line in lines:
        	circn[x],on[x],off[x]=line.split()
        	x += 1

	if on[1] < ctime and off[1] > ctime:
		logging.info('Setting Main to On')
        	ser.write('M')
	elif on[1] > ctime or off[1] < ctime:
		logging.info('Setting Main to Off')
        	ser.write('m')

	if on[2] < ctime and off[2] > ctime:
		logging.info('Setting Water to On')
        	ser.write('W')
	elif on[2] > ctime or off[2] < ctime:
		logging.info('Setting Water to Off')
        	ser.write('w')

	if on[3] < ctime and off[3] > ctime:
		logging.info('Setting Bed to On')
        	ser.write('B')
	elif on[3] > ctime or off[3] < ctime:
		logging.info('Setting Bed to Off')
        	ser.write('b')

while True:
	try:
                time.sleep(2)
                logging.info ('Begin Loop in Fullauto.py')
                os.system("python /home/pi/parsecal.py")
                ctime = time.strftime ('%Y%m%d%H%M')
                readSettings()
                testSer()
		logging.info ('Current Time')
		logging.info (ctime)
                sendSignal()
		ser.write('U')
                time.sleep(120)
    except:
                logging.critical('Loop failed due to error')
