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

sum(v1, v2)
mul(v1, v2)

print('Total time for processing: {0}s'.format(round(time.time() - start, 4)))