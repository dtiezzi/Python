## Exemplos de estruturas de repetição - while
'''
Para rodar esses exemplos, basta abrir uma tela de comando e executar o seguinte comando 
no diretório onde o arquivo foi salvo:

python exemplos_3.py

'''

# cria um função chamada loop que não recebe parâmetros
# a idéia é criar um jogo de adivinhação
from random import randint # isso importa um pacote chamado random
def loop():
	# usar o modulo para criar um valor aleatório de 0 a 100
	rand = randint(0, 100)
	guess = -1 # atribui um valor fora dos valores aleatórios
	count = 0 # vamos contar quantas tentativas para acertar
	while guess != rand:  # while loop vai rodar até que o usuário acerte o número
		guess = int(input('Descubra o valor: '))
		if guess < rand:
			print('Valor muito baixo')
		else:
			print('Valor muito alto')
		count+= 1 # cada iteração do loop soma um no count (count+= 1 é o mesmo que count = count + 1)
	# Quando sair do loop é porque o usuário acertou
	print('Parabéns! Você acertou!')
	print('Foi necessário {0} tentativas para ganhar'.format(count)) # esse é uma das formas de formatar o texto para imprimir na tela

# Veja que essa função não retorna nada
# Nestes casos, em programação chamamos isso de procedimento, não função

# chama o procedimento loop 
loop()