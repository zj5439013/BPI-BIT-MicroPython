# This File Will Loop execute.

from machine import Pin
import time

RUN = Pin(35, Pin.IN)

LED = Pin(18, Pin.OUT)
LED.value(1)

while 1 == RUN.value():
	time.sleep(0.5)
	LED.value(0)
	