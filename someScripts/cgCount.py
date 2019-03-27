def cgContent(s):
	s = s.lower()
	count = 0
	for i in s:
		if i == 'c' or i == 'g':
			count+= 1
	return (count / len(s)) * 100


def main():
	seq = input('Digite ou cole a sequencia de DNA: ')
	print('As bases CG correspondem a {0:.2f}% da sequência'.format(cgContent(seq)))

main()