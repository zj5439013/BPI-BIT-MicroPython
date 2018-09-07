# coding:utf-8
import serial.tools.list_ports

print("Looking for upload port...")
plist = list(serial.tools.list_ports.comports())

serialName = ''

if len(plist) <= 0:
    print("Serial Not Found!")
else:
    plist_0 = list(plist[len(plist) - 1])
    serialName = plist_0[0]
    print("Auto-detected:" + serialName)

FLASH_MODE = "dio"
FLASH_FREQ = "40m"

FLASH_START = "0x1000"

from esptool import main 

import sys

sys.argv = [
	'AutoFlash.py', '--chip', 'esp32', 
	'--port', serialName, 
	'--baud', '921600', 
	'erase_flash'
]

# print sys.argv

main()

import os
os.system("pause")
