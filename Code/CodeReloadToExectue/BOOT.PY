# This file is executed on every boot (including wake-boot from deepsleep)

import time
import sys
import uos
import _thread

Thread = [ False ]

def thread_check():
	index_size = uos.stat('index.py')[6]
	_thread.start_new_thread(thread_index, ())
	while(True):
		size = uos.stat('index.py')[6]
		if(size != index_size):
			index_size = size
			if(Thread[0]):
				Thread[0] = False
				while Thread[0] == False:
					time.sleep(0.5)
			_thread.start_new_thread(thread_index, ())
		time.sleep(1)
def thread_index():
	Thread[0] = True
	file = open('index.py', "r")
	code = file.read()
	file.close()
	try:
		exec(code, {'Thread' : Thread})
	except Exception as e:
		sys.print_exception(e)
	while Thread[0]:
		pass
	Thread[0] = True
	
if __name__ == "__main__":
	ThreadFileCheck = _thread.start_new_thread(thread_check, ())
