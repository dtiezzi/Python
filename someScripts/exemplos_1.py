## Exemplos de condicionais 
'''
Para rodar esses exemplos, basta abrir uma tela de comando e executar o seguinte comando 
no diretório onde o arquivo foi salvo:

python exemplos_1.py

'''

#cria uma função chamada condicional que recebe dois parâmetros
def condicional(a, b):
	# usa a estrutura condicional para retornar um resultado baseado 
	# na divisão dos dois números
	if b == 0: # checa se a divisão pode ser realizada
		return 'Valor do divisor inválido (= 0)' 
	elif a / b < 10:
		return 'nível baixo'
	elif a / b >= 10 and a / b < 20:
		return 'nível normal'
	else:
		return 'nível alto'

# cria um função pare receber os parâmetros do teclado,
# passa para a função condicional e printa o retorno na tela

def main():
	#usar o float para coverter o valor capturado do teclado (a função input captura
	# como string)
	x = float(input('Digite um número: '))
	y = float(input('Digite outro númere: '))

	# atribui o retorno da função para uma variável resultado
	resultado = condicional(x, y)

	# imprime o resultado na tela
	print(resultado)

# Chama a função principal (main)

main()