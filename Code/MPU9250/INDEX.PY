import utime
from random import randint
from machine import I2C, Pin
from mpu9250 import MPU9250
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)
sensor = MPU9250(i2c)
print("MPU9250 id: " + hex(sensor.whoami))
from Graph import BpiBitNeoPixel, NeoPixelPower
NeoPixelPower(True)
View = BpiBitNeoPixel()
X, Y, Color, Flag = 2, 2, 2, 0
while True:
	# print('acceleration:', sensor.acceleration)
	# print('gyro:', sensor.gyro)
	# print('magnetic:', sensor.magnetic)
	A = sensor.acceleration
	View.LoadXY(X, Y, (0, 0, 0))
	if(A[1] > 0 and A[1] > X and X < View.Max - 1):
		X = X + 1
	elif(A[1] < 0 and A[1] < X and X > View.Min):
		X = X - 1
	if(A[0] > 0 and A[0] > Y and Y > View.Min):
		Y = Y - 1
	elif(A[0] < 0 and A[0] < Y and Y < View.Max - 1):
		Y = Y + 1
	
	Color = Color + Flag
	if(Color == 30): Flag = -2
	elif(Color == 2): Flag = +2
	
	View.LoadXY(X, Y, (0, Color, Color))
	View.Show()
	utime.sleep_ms(200)
	
