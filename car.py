import time
from os import system
import RPi.GPIO

in1=31
in2=33
in3=35
in4=37

class Car(object):
	def __init__(self):

		self.gpio = GPIO
		self.gpio.setmode(self.gpio.BOARD)
		self.gpio.setwarnings(False)
		self.running = False

		for i in range(1, 5):
			self.gpio.setup(eval('in'+str(i)), self.gpio.OUT)
			self.gpio.output(eval('in'+str(i)), 0)

	def stop(self):
		if self.running:
			print('>>stop')
			self.gpio.output(in1, 0)
			self.gpio.output(in2, 0)
			self.gpio.output(in3, 0)
			self.gpio.output(in4, 0)
			self.running = False

	def up(self):
		print('>>up')
		self.gpio.output(in1, 1)
		self.gpio.output(in2, 0)
		self.gpio.output(in3, 0)
		self.gpio.output(in4, 1)
		self.running = True
		
	def down(self):
		print('>>down')
		self.gpio.output(in1, 0)
		self.gpio.output(in2, 1)
		self.gpio.output(in3, 1)
		self.gpio.output(in4, 0)
		self.running = True

	def left(self):
		print('>>left')
		self.gpio.output(in1, 0)
		self.gpio.output(in2, 1)
		self.gpio.output(in3, 0)
		self.gpio.output(in4, 1)
		self.running = True

	def right(self):
		print('>>right')
		self.gpio.output(in1, 1)
		self.gpio.output(in2, 0)
		self.gpio.output(in3, 1)
		self.gpio.output(in4, 0)
		self.running = True


class DebugGPIO(object):
	def BOARD(self):
		pass
	def OUT(self):
		pass
	def setmode(self, param):
		pass
	def setwarnings(self, param):
		pass
	def setup(self, param, param2):
		pass
	def output(self, param, param2):
		pass