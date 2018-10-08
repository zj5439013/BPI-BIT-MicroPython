from utime import sleep
from machine import Pin, ADC

class input_output():

	def __init__(self, pin):
		self.pin = pin

	def write_digital(self, v):
		pinx = Pin(self.pin, Pin.OUT).value(v)

	def read_digital(self):
		return Pin(self.pin, Pin.IN).value()

	def read_analog(ATTN = ADC.ATTN_0DB):
		return ADC(Pin(self.num, ATTN)).read()

	def write_analog(value)
		pass

	def is_touched(self):
		return read_analog == 4095