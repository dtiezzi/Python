import time
import matplotlib.pyplot as plt

def fibonacci2(n):
	l= []
	for i in range(n+1):
		if i == 0:
			l.append(0)
		elif i == 1:
			l.append(1)
		else:
			l.append((l[i - 2]) + (l[i - 1]))
	return l[n]

num= int(input('Type the nth sequence in Fibonacci: '))

start = time.time()
pstart = time.process_time()

fibo_rec_times = []
fibo_time_process = []
for num in range(num):
	pstart1 = time.process_time()
	res= fibonacci2(num)
	pstop1 = time.process_time()
	fibo_time_process.append(pstop1 - pstart1)

print(fibo_rec_times, fibo_time_process)
print("#" * 40 + '\n') 
print("The {0}th number in Fibonacci sequence is {1}.".format(num, res))
print('\n' + "#" * 40 + '\n')

stop = time.time()
pstop= time.process_time()

print("Bellow is the total time to run this program and the time CPU spent to calculate the Fibonacci sequence: \n")

print("Total time: {0:.6}, CPU time: {1:.6}".format(stop - start, pstop - pstart))

print('\n' + "#" * 40 + '\n')


plt.plot(range(num + 1), fibo_time_process)
plt.ylabel('time em seconds')
plt.show()

