from utime import sleep
from machine import Pin ,ADC

DEBUG = False

class input_output():

	def __init__(self, pin):
		print("input_output" if DEBUG else "\b")
		self.pin = pin

	def write_digital(self, v):
		print("write_digital" if DEBUG else "\b")
		pinx = Pin(self.pin, Pin.OUT).value(v)

	def is_touched(self):
		print("is_touched" if DEBUG else "\b")
		adc = ADC(Pin(self.pin, Pin.IN))
		adc.atten(ADC.ATTN_0DB)
		return adc.read() == 4095

pin0=input_output(25)
pin1=input_output(32)
pin2=input_output(33)
pin3=input_output(13)
pin4=input_output(16)
pin5=input_output(35)
pin6=input_output(12)
pin7=input_output(14)
pin8=input_output(16)
pin9=input_output(17)
pin10=input_output(26)
pin11=input_output(27)
pin12=input_output(2)
pin13=input_output(18)
pin14=input_output(19)
pin15=input_output(23)
pin16=input_output(5)
pin19=input_output(22)
pin20=input_output(21)
