def calc(a, b, c):
	if c == '+':
		return a + b
	elif c == '-':
		return a - b
	elif c == '/':
		if b == 0:
			res = '[ERR]...Não eh possível divisão por 0!'
			return res
		else:
			return a / b
	elif c == '*':
		return a * b
	else:
		res = '[ERR]...Operação não disponível!'
		return res

def menu():
	print(
'''
Selecione uma opção abaixo:
1 - Digite "+" para soma;
2 - Digite "-" para subtração;
3 - Digite "/" para divisão;
4 - Digite "*" para nultiplicação;
'''
		)

def main():
	op = 's'
	while op == 's':
		menu()
		opr = input()
		x = float(input('Digite um número: '))
		y = float(input('Digite outro número: '))
		print('Resultado de {0} {1} {2} = {3}'.format(x, opr, y, calc(x, y, opr)))
		op = input('Realizar outra operação (s/n)?')

	print("Desconectado da Calculadora!")

main()