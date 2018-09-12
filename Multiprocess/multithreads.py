import threading
import time

start = time.time()
def sum(val1, val2):
	for i in range(10000000):
		print(val1 + val2, end=" ")

def mul(val1, val2):
	for i in range(10000000):
	 print(val1 * val2, end=" ")


v1 = 3

v2 = 5

thread1 = threading.Thread(target=sum, args=(v1, v2))
thread2 = threading.Thread(target=mul, args=(v1, v2))

# Start new Threads
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('Total time for processing: {0}s'.format(round(time.time() - start, 4)))
