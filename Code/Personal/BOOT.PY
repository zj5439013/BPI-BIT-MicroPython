# This file is executed on every boot (including wake-boot from deepsleep)

import time
import sys
import uos
import _thread

def thread_check():
	index_size = 0
	while(True):
		size = uos.stat('index.py')[6]
		if(size != index_size):
			print("File Update Now Reload...")
			_thread.start_new_thread(thread_main, ())
			index_size = size
		time.sleep(0.5)
		
def thread_main():
	file = open('index.py', "r")  
	code = file.read()
	file.close()  
	exec(code)

if __name__ == "__main__":
	ThreadFileCheck = _thread.start_new_thread(thread_check, ())
	
	