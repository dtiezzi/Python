
## Controle de fluxo e estruturas de repetição

### Condicionais

**if..else**

Em lógica de programação utilizamos estruturas condicionais para controle de fluxo.
As condições **if** e **else** são utilizadas para executar blocos de código somente em determinadas situações.


```python
# if .. else

x = 5
y = 3
if x * y > 10: # note o uso de um operador de comparação
    z = x + y # note a identação. Vamos falar sobre isso no curso.
print(z)
```

    8



```python
# Se houver duas possibilidades, usa-se if e else
if x * y > 20:
    z = x + y
else:
    z = x - y
print(z)
```

    2



```python
# Se houver mais de duas possibilidades, usamos elif

if x * y < 10:
    z = x + y
elif x * y >= 10 and x * y < 20: # note o uso do operador lógico and. 
    z = x - y
else:
    z =  x * y
print(z)
```

    2


### Estruturas de repetição

**for e while**

Em lógica de programação utilizamos estruturas de repetição para automatizar tarefas. O **for** geralmente é utilizado quando sabemos o número exato de repetições. Já o **while** é mais utilizado em situações onde o programador não tem o controle de quantas repetições irão ocorrer. Vamos ver como eles funcionam e exemplos.


```python
# for
# existem várias maneiras de utilizar o for em Python
# aqui vamos utilizar a função range(), que retorna valores sequenciais. Vejamos
print(list(range(1,11))) # list() é uma função que converte uma sequência em uma lista.
# O range recebe até três parâmetros
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



```python
# Veja que passamos os parâmetros 1 e 11 para a função. E ela retornou valores de 1 a 10. Se quisermos 10 valores:
print(list(range(10))) # aqui só um parâmetro. Vou discutir isso no curso
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



```python
# Agora podemos utilizar o range para controlar o número de reprtições em um for
for i in range(10): # essa é a sintaxe básica para o for
    print(i, end = ' ') # note a identação aqui também.O end é um argumento da função print()
```

    0 1 2 3 4 5 6 7 8 9 


```python
# Veja que repetimos a ação (print(i)) 10 vezes.
# Podemos ler assim: para i com valores entre 0 e 10 imprima i
# Assim podemos utilizar isso para imprimir a tabuada do 7, por exemplo
for i in range(1, 11):
    print(7 * i, end = ' ')
```

    7 14 21 28 35 42 49 56 63 70 


```python
# Melhorando nossa tabuada do 7
for i in range(1, 11):
    print('7 x {0} = {1}'.format(i, 7 * i))
```

    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    7 x 4 = 28
    7 x 5 = 35
    7 x 6 = 42
    7 x 7 = 49
    7 x 8 = 56
    7 x 9 = 63
    7 x 10 = 70



```python
# É possivel aninhar mais de uma estrutura
for i in range(10):
    for j in range(10):
        print(i, j, end = '')
    print()
```

    0 00 10 20 30 40 50 60 70 80 9
    1 01 11 21 31 41 51 61 71 81 9
    2 02 12 22 32 42 52 62 72 82 9
    3 03 13 23 33 43 53 63 73 83 9
    4 04 14 24 34 44 54 64 74 84 9
    5 05 15 25 35 45 55 65 75 85 9
    6 06 16 26 36 46 56 66 76 86 9
    7 07 17 27 37 47 57 67 77 87 9
    8 08 18 28 38 48 58 68 78 88 9
    9 09 19 29 39 49 59 69 79 89 9



```python
# Todo o bloco de código que está identado será repetido. Se tirar a identação, acaba o bloco de código da repetiçaõ
for i in range(5):
    print(i)
    print('Bom dia')
    x = 2 * 3**i
    print(x)
print('Acabou o for loop!')
```

    0
    Bom dia
    2
    1
    Bom dia
    6
    2
    Bom dia
    18
    3
    Bom dia
    54
    4
    Bom dia
    162
    Acabou o for loop!


# Exercício #1 

**Escreva um programa que imprime toda a tabuada de 1 a 10**


```python
for i in range(1, 11):
    for j in range(1, 11):
        print('{0} X {1} = {2} '.format(j, i, j * i), end = ' ')
    print()
```

    1 X 1 = 1  2 X 1 = 2  3 X 1 = 3  4 X 1 = 4  5 X 1 = 5  6 X 1 = 6  7 X 1 = 7  8 X 1 = 8  9 X 1 = 9  10 X 1 = 10  
    1 X 2 = 2  2 X 2 = 4  3 X 2 = 6  4 X 2 = 8  5 X 2 = 10  6 X 2 = 12  7 X 2 = 14  8 X 2 = 16  9 X 2 = 18  10 X 2 = 20  
    1 X 3 = 3  2 X 3 = 6  3 X 3 = 9  4 X 3 = 12  5 X 3 = 15  6 X 3 = 18  7 X 3 = 21  8 X 3 = 24  9 X 3 = 27  10 X 3 = 30  
    1 X 4 = 4  2 X 4 = 8  3 X 4 = 12  4 X 4 = 16  5 X 4 = 20  6 X 4 = 24  7 X 4 = 28  8 X 4 = 32  9 X 4 = 36  10 X 4 = 40  
    1 X 5 = 5  2 X 5 = 10  3 X 5 = 15  4 X 5 = 20  5 X 5 = 25  6 X 5 = 30  7 X 5 = 35  8 X 5 = 40  9 X 5 = 45  10 X 5 = 50  
    1 X 6 = 6  2 X 6 = 12  3 X 6 = 18  4 X 6 = 24  5 X 6 = 30  6 X 6 = 36  7 X 6 = 42  8 X 6 = 48  9 X 6 = 54  10 X 6 = 60  
    1 X 7 = 7  2 X 7 = 14  3 X 7 = 21  4 X 7 = 28  5 X 7 = 35  6 X 7 = 42  7 X 7 = 49  8 X 7 = 56  9 X 7 = 63  10 X 7 = 70  
    1 X 8 = 8  2 X 8 = 16  3 X 8 = 24  4 X 8 = 32  5 X 8 = 40  6 X 8 = 48  7 X 8 = 56  8 X 8 = 64  9 X 8 = 72  10 X 8 = 80  
    1 X 9 = 9  2 X 9 = 18  3 X 9 = 27  4 X 9 = 36  5 X 9 = 45  6 X 9 = 54  7 X 9 = 63  8 X 9 = 72  9 X 9 = 81  10 X 9 = 90  
    1 X 10 = 10  2 X 10 = 20  3 X 10 = 30  4 X 10 = 40  5 X 10 = 50  6 X 10 = 60  7 X 10 = 70  8 X 10 = 80  9 X 10 = 90  10 X 10 = 100  



```python
# while é uma estrutura que repete enquanto um condição for verdadeira
# Por isso, devemos ter cuidado para não entrar em um loop infinito
x = 0 # criamos um contador
while x <= 5: # a condição é testada. Se retornar True, executa o bloco
    print(x) 
    x+=1 # aqui estou incrementando o x um a um a cada iteração. Caso contrário, esse loop seria infinito
```

    0
    1
    2
    3
    4
    5



```python
# Para exemplificar uma situação clássica onde o while pode ser utilizado vamos ver a função input().
# Essa função recebe uma entrada do teclado. Vamos perguntar para o usuário quantas repetição ele quer em um loop
resposta = input('Digite o número de repetições: ') # o imput() sempre cria uma variável do tipo string (texto)
resposta = int(resposta) # a função int() converte uma string para número inteiro

for i in range(resposta):
    print(i)
```

    Digite o número de repetições: 3
    0
    1
    2



```python
# Assim, podemos usar o while para criar um jogo de adivinha
# Iremos repetir a checagem até o usuário acertar o número.
# Neste caso, não sabemos quantas tentativas o usuário irá utilizar para acertar.
# Por isso, aqui é melhor utilizar o while, e não o for
# eu vou utilizar um pacote para gerar um número aleatório
# Não se preocupe com isso agora, iremos ver isso logo mais
from random import randint

resp = 'errada'
num = randint(0,101) # gera um número aleatório de 0 a 100
n = 1 # contador
while resp == 'errada': 
    op = int(input('Digite um número de 0 a 100: ')) # veja que já tranformei o input em um número inteiro
    if op == num:
        print('Parabéns, voce acertou o número {0} em {1} tentativas.'.format(num, n))
        resp = 'certa'  # modifica a resposta para que a condição do while seja False
    else:
        if op < num:
            print('Ops! Você digitou um número muito baixo.')
        else:
            print('Ops! |Você digitou um número muito alto.')
        n+=1 # incrementa a contagem de tentativas
    
```

    Digite um número de 0 a 100: 55
    Ops! Você digitou um número muito baixo.
    Digite um número de 0 a 100: 77
    Ops! Você digitou um número muito baixo.
    Digite um número de 0 a 100: 88
    Ops! Você digitou um número muito baixo.
    Digite um número de 0 a 100: 99
    Ops! |Você digitou um número muito alto.
    Digite um número de 0 a 100: 90
    Ops! Você digitou um número muito baixo.
    Digite um número de 0 a 100: 93
    Ops! |Você digitou um número muito alto.
    Digite um número de 0 a 100: 91
    Ops! Você digitou um número muito baixo.
    Digite um número de 0 a 100: 92
    Parabéns, voce acertou o número em 8 tentativas.



```python
# Em python o for e o while têm uma conotação diferente de outras linguagens (como em C, por exemplo)
# Ele funciona como um método de iteração
# Assim, podemos utilizar eles para iteragir como uma estrutura de dados.
# Em dicionário, temos que usar a chave como index.

minhaLista = ['a', 'b', 'c']
for i in minhaLista:
    print(i)
print('\n') # o \n é o correspondente do 'ENTER' do seu teclado. Eu seja, pula uma linha
minhaTuple = ('a', 'b', 'c')
for i in minhaTuple:
    print(i)
print('\n')
meuSet = {'a', 'b', 'c'}
for i in meuSet:
    print(i)
print('\n')
meuDic = {'a': 1, 'b' : 2, 'c' : 3}
for key in meuDic:
    print("{0} = {1}".format(key, meuDic[key]))
```

    a
    b
    c
    
    
    a
    b
    c
    
    
    c
    b
    a
    
    
    a = 1
    b = 2
    c = 3

