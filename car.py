
import time
from os import system
from RPi import GPIO


in1=33
in2=35
in3=37
in4=36


class Car(object):

	def __init__(self):

		self.gpio = GPIO
		self.gpio.setmode(gpio.BOARD)
		self.gpio.setwarnings(False)

		for i in range(4):
			self.gpio.setup(in1, gpio.OUT)

			self.gpio.output(in1, 0)





# -*- coding:utf-8 -*-

import RPi.GPIO
import time
from os import system

in1=33
in2=35
in3=37
in4=36

in5=3 #led灯

gpio=RPi.GPIO

power=False


def powerON():
	global power,gpio,in1,in2,in3,in4,in5
	
	gpio.setmode(gpio.BOARD)
	gpio.setwarnings(False)

	gpio.setup(in1, gpio.OUT)
	gpio.setup(in2, gpio.OUT)
	gpio.setup(in3, gpio.OUT)
	gpio.setup(in4, gpio.OUT)
	gpio.setup(in5, gpio.OUT)

	gpio.output(in1, 0)
	gpio.output(in2, 0)
	gpio.output(in3, 0)
	gpio.output(in4, 0)
	gpio.output(in5, 1)

	power=True
	print '>>>>>>>>>>>>>>> PowerON'

def powerOFF():
	global power,gpio
	gpio.cleanup()
	power=False
	print '>>>>>>>>>>>>>>> PowerOFF'



def ledOn():
	global power,gpio,in1,in2,in3,in4,in5
	if not power:
		print 'PowerOFF!'
		return
	gpio.output(in5, 0)

def ledOff():
	global power,gpio,in1,in2,in3,in4,in5
	if not power:
		print 'PowerOFF!'
		return
	gpio.output(in5, 1)

def forward():
	global power,gpio,in1,in2,in3,in4
	if not power:
		print 'PowerOFF!'
		return
	#print '>>forward'

	gpio.output(in1, 1)
	gpio.output(in2, 0)
	gpio.output(in3, 0)
	gpio.output(in4, 1)
	
def back():
	global power,gpio,in1,in2,in3,in4
	if not power:
		print 'PowerOFF!'
		return
	#print '>>back'

	gpio.output(in1, 0)
	gpio.output(in2, 1)
	gpio.output(in3, 1)
	gpio.output(in4, 0)

def left():
	global power,gpio,in1,in2,in3,in4
	if not power:
		print 'PowerOFF!'
		return
	#print '>>left'

	gpio.output(in1, 0)
	gpio.output(in2, 1)
	gpio.output(in3, 0)
	gpio.output(in4, 1)

def right():
	global power,gpio,in1,in2,in3,in4
	if not power:
		print 'PowerOFF!'
		return
	#print '>>right'

	gpio.output(in1, 1)
	gpio.output(in2, 0)
	gpio.output(in3, 1)
	gpio.output(in4, 0)

def stop():
	global power,gpio,in1,in2,in3,in4
	if not power:
		print 'PowerOFF!'
		return
	#print '>>stop'

	gpio.output(in1, 0)
	gpio.output(in2, 0)
	gpio.output(in3, 0)
	gpio.output(in4, 0)

def shutdown():
	system('poweroff')
