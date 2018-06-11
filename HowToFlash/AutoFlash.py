# coding:utf-8
import serial.tools.list_ports

print("Looking for upload port...")
plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print("Serial Not Found!")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName, 9600, timeout=60)
    print "Auto-detected:" + serialFd.name
    serialFd.close()
	
FLASH_MODE = "dio"
FLASH_FREQ = "40m"

FLASH_START = "0x1000"

from esptool import main 

import sys

sys.argv = [
	'AutoFlash.py', '--chip', 'esp32', 
	'--port', serialFd.name, 
	'--baud', '460800',  # 1152000
	'write_flash', '-z',
	'--flash_mode', FLASH_MODE, 
	'--flash_size', '4MB',
	'--flash_freq', FLASH_FREQ,
	FLASH_START, 'firmware.bin'
]

# print sys.argv

main()

import os
os.system("pause")
