def probeHib(seq, p):
	seq = seq.lower()
	p = p.lower()

	ml = []
	for i in range(len(seq) - len(p)):	
		if seq[i] == p[0]:
			if p == seq[i:i+len(p)] or p == seq[i-len(p):i]:
				ml.append(i)

	if len(ml) != 0:
		return ml
	else:
		return 'no match'

def readFasta(fasta):
	with open(fasta, 'r') as file:
		fastaSeq = ''
		for line in file:
			if line[0] != '>':
				fastaSeq+= line
		return fastaSeq

def main():
	seqPath = input('Digite o nome do arquivo .fasta: ')
	s = readFasta(seqPath)
	prob = input('Digite ou cole a sequência do probe:')
	res = probeHib(s, prob)
	if res == 'no match':
		print('Não existem locais de hibridização do probe nesta sequência.')
	else:
		print('O probe hibridiza perfeitamente na(s) posição(ões) {0} da sequência.'.format(', '.join(str(x) for x in res)))

main()