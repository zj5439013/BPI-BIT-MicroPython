from utime import sleep
from machine import Pin, ADC

class input_output():

	def __init__(self, pin):
		self.pin = pin

	def write_digital(self, v):
		pinx = Pin(self.pin, Pin.OUT).value(v)

	def is_touched(self):
		adc = ADC(Pin(self.num, Pin.IN))
		adc.atten(ADC.ATTN_0DB)
		return adc.read() == 4095