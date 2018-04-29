
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
