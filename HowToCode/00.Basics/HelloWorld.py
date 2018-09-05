from machine import Pin
import time
LED = Pin(18, Pin.OUT)
while True:
	LED.value(1) # Let the LED on.