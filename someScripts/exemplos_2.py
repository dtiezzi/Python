## Exemplos de estruturas de repetição 
'''
Para rodar esses exemplos, basta abrir uma tela de comando e executar o seguinte comando 
no diretório onde o arquivo foi salvo:

python exemplos_2.py

'''

# cria um função chamada loop que recebe dois parâmetros

def loop(a, b):
	# criando um 'nested loop'. Veja que temos um for dentro do outro
	# desta froma, iremos executar o for 2 a vezes.
	# Vamos usar isso para criar um estrutura multidimencional
	# Pode ser um matrix a x b
	mat = [] # criei uma lista vazia que será minha matrix a x b
	for i in range(a): # repete a vezes a instrução. O valor a = número de linhas da matrix
		l = [] # criei um lista vazia que será as linhas de nossa matrix
		for j in range(b): # repete b vezes a instrução. O valor b = número de colunas da matrix
			x = int(input('Digite o valor: ')) # guarda um valor inteiro do teclado
			l.append(x) # insere o valor de x na lista l
		mat.append(l) # insere a lista l na lista mat
	return mat# retorna a matrix com os valores inseridos pelo usuário

# criar um função para criar e imprimir a matrix que criamos

def main():
	# guara os valores referentes ao tamanho da matriz
	n1 = int(input('Digite o número de linhas da matriz: ')) 
	n2 = int(input('Digite o número de colunas da matriz: '))

	m = loop(n1 , n2) # cria a matriz e guarda o valor em mat

	# inprime a matriz
	for linha in m:
		for valor in linha:
			print(valor, end=' ') # o end com um espaço faz imprimir na mesma linha
		print('') # faz a proxima linha ser impressa abaixo

# chama a função main
main()