
## Tipos de dados, operadores e estruturas de dados em python


```python
#Criar variável
x = 10
y = 5
print('O valor de x é:')
print(x)
print('O endereço de x é: ')
print(id(x))
print('O valor de y é:')
print(y)
print('O endereço de y é: ')
print(id(y))
```

    O valor de x é:
    10
    O endereço de x é: 
    11381760
    O valor de y é:
    5
    O endereço de y é: 
    11381600



```python
#Melhorar a função print() com a função format()
print('O valor de x é: {0} e o endereço de x na memória é: {1}'.format(x, id(x)))
print('O valor de y é: {0} e o endereço de y na memória é: {1}'.format(y, id(y)))
```

    O valor de x é: 10 e o endereço de x na memória é: 11381760
    O valor de y é: 5 e o endereço de y na memória é: 11381600



```python
#Tipos de variáveis
#Numérica
#inteiro (int)
type(x)
#(float)
z = 1.0
type(z)
#String (str)
letra = 'a'
texto = 'Bom dia'
type(letra)
type(texto)

#Boolena
t = True
f = False
```

## Operadores aritméticos


```python
%%html
<style>
    th {
        font-size: 20px;
    }
    td {
        font-size: 20px;
    }
    table {
        display: inline-block;
    }
</style>
```


<style>
    th {
        font-size: 20px;
    }
    td {
        font-size: 20px;
    }
    table {
        display: inline-block;
    }
</style>



| Operador | Nome | Exemplo |
|---|---|---|
| + | Adição | x + y |
| - | Subtração | x - y |
| * | Multiplicação | x * y |
| / | Divisão | x / y |
| % | Modulus | x % y |
| ** | Exponenciação | x ** y |
| // | Divisão inteira | x // y |

## Operadores de atribuição

| Operador | Exemplo | O mesmo que |
|---|---|---|
| = | x = 5 | x = 5 |
| += | x += 1 | x = x + 1 |
| -= | x -= 1 | x = x - 1 |

## Operadores de comparação

| Operador | Nome | Exemplo |
|---|---|---|
| == | Igual | x == 5 |
| != | Diferente | x != 1 |
| > | Maior | x > 1 |
| < | Menor | x < 1 |
| >= | Maior ou igual | x >= 1 |
| <= | Menor ou igual | x <= 1 |

## Operadores lógicos

| Operador | Descrição | Exemplo |
|---|---|---|
| and | Retorna True se ambos forem verdadeiros | x > 5 and x < 10 |
| or | Retorna True se um deles for verdadeiro | x == 1 or x == 5 |
| not | Reverte o resultado da operação | not(x > 5 and x < 10) |

## Operadores de identidade

| Operador | Descrição | Exemplo |
|---|---|---|
| is | Retorna True se ambos forem o mesmo objeto | x is y |
| is not | Retorna True se não forem o mesmo objeto | x is not y |

## Operadores de associação

| Operador | Descrição | Exemplo |
|---|---|---|
| in | Retorna True se o valor estiver presente no objeto | x is y |
| not in | Retorna True se o valor não estar presente no objeto | x is not y |

## Operadores binários

| Operador | Nome | Descrição |
|---|---|---|
| & | AND | Cada bit para 1 se ambos forem 1 |
| | | OR | Cada bit para 1 se pelo menos um for 1 |
| ^ | XOR | Cada bit para 1 se apenas um for 1 |
| ~ | NOT | Inverte os bits |

## Estruturas de dados


```python
# Lista
l1 = [] # lista vazia
l2 = [1,2,3,4]
l3 = ['a', 'b', 'c']
l4 = [1,'a',23.0, 'bom dia']
l5 = [[1,2,3], ['a', 'b', 'c']]
print(l5)
```

    [[1, 2, 3], ['a', 'b', 'c']]



```python
# Tuple
t1 = ()
t2 = (1,2,3)
t3 = ('a', 'b','c')
t4 = (1, 'a', 'fmrp', 1.4)
print(t4)
```

    (1, 'a', 'fmrp', 1.4)



```python
# Sets
s0 = {}
s1 = {3, 4, 6}
print(s1)
```

    {3, 4, 6}



```python
# Dicionário
d0 = {}
d1 = {'a' : 1, 'c' : 3, 'b': 2}
print(d1)
```

    {'a': 1, 'c': 3, 'b': 2}


- **Lista** é ordenada, mutável. Permite duplicatas;
- **Tuple** é ordenada e imutável. Permite duplicatas;
- **Set** é não ordenado e não indexado. Não permite duplicatas;
- **Dicionário** é não ordenado, é mutável e indexado. Não permite duplicatas.


```python
## Ordenado - a sequencia se mantém e existe um indexação
# Em Python, o index começa pelo 0

minhaLista = [10,34,12,45,23]
print('Index 0 = {0}, index 3 = {1}, index -1 = {2}'.format(minhaLista[0], minhaLista[3], minhaLista[-1]))
```

    Index 0 = 10, index 3 = 45, index -1 = 23



```python
## Imutável - os valores não podem ser modificados

minhaLista[1] = 'teste'
print(minhaLista)
```

    [10, 'teste', 12, 45, 23]



```python
minhaTuple = (10, 34, 12, 45, 23)
minhaTuple[1] = 'teste'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-51847eed12bf> in <module>
          1 minhaTuple = (10, 34, 12, 45, 23)
    ----> 2 minhaTuple[1] = 'teste'
    

    TypeError: 'tuple' object does not support item assignment



```python
# Não ordenado - os valores podem aparecer em qualquer ordem e não há uma indexação

meuSet0 = {34, 43, 54, 2, 43, 23, 54, 1100, 34}
print(meuSet0)
```

    {2, 34, 43, 1100, 54, 23}



```python
print(meuSet0[2])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-13-7ca06424c852> in <module>
    ----> 1 print(meuSet0[2])
    

    TypeError: 'set' object is not subscriptable



```python
# Não permite duplicatas

meuSet1 = {2, 4, 5, 2 ,7}
print(meuSet1)
```

    {2, 4, 5, 7}



```python
# Dicionário é baseado em chave : valor. A chave é o índice

meuDic = {'Nome' : 'Daniel', 'Sobrenome' : 'Tiezzi', 'idade' : 47, 'nascimento' : '29/04/1972'}
print(meuDic)
print(meuDic['idade'])
```

    {'Nome': 'Daniel', 'Sobrenome': 'Tiezzi', 'idade': 47, 'nascimento': '29/04/1972'}
    47

