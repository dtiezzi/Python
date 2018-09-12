import multiprocessing
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

p1 = multiprocessing.Process(target=sum, args=(v1, v2))
p2 = multiprocessing.Process(target=mul, args=(v1, v2))

#start multiprocess
p1.start()
p2.start()

p1.join()
p2.join()

print('Total time for processing: {0}s'.format(round(time.time() - start, 4)))