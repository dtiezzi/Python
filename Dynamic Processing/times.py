import time
import matplotlib.pyplot as plt

def fibonacci1(n):
	recs[0]+= 1
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci1(n - 1) + fibonacci1(n - 2)

num= int(input('Type the nth sequence in Fibonacci: '))

start = time.time()
pstart = time.process_time()

fibo_rec_times = []
fibo_time_process = []
for num in range(num):
	pstart1 = time.process_time()
	recs = [0]
	res= fibonacci1(num)
	r = recs[0] - 1
	pstop1 = time.process_time()
	fibo_rec_times.append(r)
	fibo_time_process.append(pstop1 - pstart1)

print(fibo_rec_times, fibo_time_process)
print("#" * 40 + '\n') 
print("The {0}th number in Fibonacci sequence is {1} and, in a recursive mode, it was necessary {2} recursions to calculate it.".format(num, res, r))
print('\n' + "#" * 40 + '\n')

stop = time.time()
pstop= time.process_time()

print("Bellow is the total time to run this program and the time CPU spent to calculate the Fibonacci sequence: \n")

print("Total time: {0:.6}, CPU time: {1:.6}".format(stop - start, pstop - pstart))

print('\n' + "#" * 40 + '\n')

plt.subplot(1, 2, 1)
plt.plot(range(num + 1), fibo_time_process)
plt.ylabel('time em seconds')

plt.subplot(1, 2, 2)
plt.plot(range(num + 1), fibo_rec_times)
plt.ylabel('# of recurtions')
plt.show()

