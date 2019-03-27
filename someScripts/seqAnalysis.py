# Cria o dicionário com os codons - AAs
codons = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}


# tradução
def protein(cods, seq):
    seq = seq.upper()
    prot = []
    for i in range(0,len(seq) - 3,3):
        cod = seq[i:i + 3]
        try:
            aa = cods[cod]
            if aa == 'STOP':
                prot.append(aa)
                break
            prot.append(aa)
        except KeyError:
            aa = 'NA'
            prot.append(aa)
    return prot

def readFasta(fasta):
    with open(fasta, 'r') as file:
        fastaSeq = ''
        for line in file:
            if line[0] != '>':
                fastaSeq+= line.rstrip("\n")
        return fastaSeq

def main():
    seqPath = input('Digite o nome do arquivo com a sequencia de referência em fasta: ')
    geneName = input('Digite o nome do gene: ')
    s = readFasta(seqPath)
    protSeq = protein(codons, s)
    #print(''.join(protSeq))
    geneRef = ''.join(protSeq)
    new = 's'
    while new == 's':
        seqAltPath = input('Digite o nome do arquivo com a sequencia alternativa em fasta: ')
        sa = readFasta(seqAltPath)
        protAltSeq = protein(codons, sa)
        geneAlt = ''.join(protAltSeq)
        for p, (i, j) in enumerate(zip(geneRef, geneAlt)):
            if i != j:
                #print(geneAlt[p:p+5])
                if ''.join(geneAlt[p:p+5]) == 'STOP':
                    print(i, ''.join(geneAlt[p:p+5]))
                    break
                else:
                    print(i, j)
        new = input('Analisar outra sequencia (s/n)?').lower()

main()