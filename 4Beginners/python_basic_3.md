
## Funções e Classes

**Funções**

Nós já utilizamos uma série de funções até agora, como a print() e a input(). Essas funções são nativas no python.
Nós podemos criar nossas próprias funções. As funções são criadas apra realizar uma tarefa específica.
Assim, podemos reutilizá-las sem que seja preciso reescrever o código.
Funções devem retornar uma variável. Caso contrário, ela não pode ser denominada de função, e sim de procedimento.
Vamos ver alguns exemplos e vamos discutir os benefícios desta abordagem.


```python
# A sintaxe clássica de uma função em python é:

def nome_da_função(argumentos):
    seu_codigo = null 
    return seu_codigo
```


```python
# Vamos criar uma função para retornar um número elevado a um determinado valor
# vamos chamá-la de exponencial

def exponencial(a, b): # define a função que recebe dois valores a e b
    return a**b # retorna a elevado a b
```


```python
# Assim que criamos a função, podemos utilizá-la agora. 
# Vamos pegar dois valores inseridos pelo usuário e usar a função para retornar um valor elevado ao outro

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
z = exponencial(x, y) # z será o valor de x elevado a y
print(z)
```

    Digite um número: 3
    Digite outro número: 5
    243


**Classes**

Python é uma linguagem orientada a objeto. Virtualmente, tudo em python é um objeto de alguma classe. Por exemplo, quando criamos uma lista de nome **l1**, estamos criando um objeto de nome **l1** da classe lista.
Os objetos possuem atributos e métodos. Os atributos são características do objeto e os métodos são funções que modificam os atributos da classe.
Esse conceito de orientação  objeto pode ser um tanto abstrato, mas é importante termos uma noção para entendermos como alguns métos podem ser aplicados à alguns objetos.
Não vamos entrar na questão básica de como criar classes. Mas a idéia aqui é saber como podemos utilizar alguns métodos próprios de alguns objetos como listas ou sets.


```python
# Vamos criar uma lista l1
l1 = [2,3,4]
# podemos utilizar a função type() para checar que classe o objeto pertence
print(type(l1))
```

    <class 'list'>



```python
# podemos utilizar a função dir() para checar todos os atributos e métodos da nossa classe
print(dir(l1))
```

    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']



```python
# De append até sort são métodos da classe. E assim podemos utilizar eles para modificar ou extrair infromações dos atributos da classe.
# Veja que o atributo '__iter__' faz a iteração entre os valores da lista
print(list(l1.__iter__()))
# e o método 'append' pode modificar isso. Ele insere um novo valor no final da lista
l1.append(75)
print(l1)
```

    [2, 3, 4]
    [2, 3, 4, 75]



```python
# O método 'index' retorna o índice de um elemento na lista
print(l1.index(4))
```

    2


**Tente utilizar o dir() em objetos de diferentes classes como tuple, sets, dicionários... . Você verá que cada classe tem seus atributos e classes.**


```python
# Podemos criar nossas próprias classes. O objetivo não é aprofundar em orientação a objeto aqui.
# Mas vamos ver como funciona.
# Vamos supor que queremos criar uma classe Paciente que tem cinco atributos:
# nome, idade, peso, altura e imc (índice de massa corpórea).

class Paciente:
    
    def __init__(self, nome, idade, peso, altura): # essa é a função que chamamos de construtor
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.imc = 0
        
p1 = Paciente('Daniel', 45, 93, 1.79)
print(dir(p1))
```

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'altura', 'idade', 'imc', 'nome', 'peso']



```python
# Veja que o imc tem um valor fixo = 0. Precisamos de um método para modificar isso.
# vamos refazer a classe com o método imCalc
class Paciente:
    
    def __init__(self, nome, idade, peso, altura): # essa é a função que chamamos de construtor (__init__). 
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.imc = 0
        
    def imCalc(self): # essa função calcula o IMC
        self.imc = self.peso / self.altura**2
        return self.imc
    
    def imcRes(self): # interpreta o resultado do calculo do IMC
        if self.imc <= 20:
            res = 'peso abaixo do normal'
        elif self.imc > 20 and self.imc <= 25:
            res = 'peso normal'
        elif self.imc > 25 and self.imc <= 30:
            res = 'sobrepeso'
        elif self.imc > 30 and self.imc <= 40:
            res = 'obeso'
        else:
            res = 'obeso mórbido'
        return res
    
p1 = Paciente('Daniel', 45, 93, 1.79) # cria um objeto p1 da classe Paciente. É necessário passar os 4 parâmetros

print('Sr(a) {0}. Seu IMC é {1:.2f}. \nIsso significa que você é classificado como {2}.'
      .format(p1.nome ,p1.imCalc(), p1.imcRes()))
```

    Sr(a) Daniel. Seu IMC é 29.03. 
    Isso significa que você é classificado como sobrepeso.



```python
# Podemos criar novos objetos da classe Paciente agora
# para acessar os atributos ou métodos usamos o p1.algo
p2 = Paciente('Isabela', 21, 53, 1.60)
p2.imCalc()
p2.imcRes()
# veja acima que existe um atributo nativo '__dict__'
# ele é um dicionário com cada atributo (chave) e seu respectivo valor
print(p2.__dict__)
```

    {'nome': 'Isabela', 'idade': 21, 'peso': 53, 'altura': 1.6, 'imc': 20.703124999999996}



```python
#Podemos imprimir os dados de uma forma mais adequada
print('Paciente: {0} \nIdade: {1} \nPeso: {2} \nAltura: {3} \nIMC: {4:.2f} \nClassificado como {5}'.format(
    p2.nome, p2.idade, p2.peso, p2.altura, p2.imc, p2.imcRes()))
```

    Paciente: Isabela 
    Idade: 21 
    Peso: 53 
    Altura: 1.6 
    IMC: 20.70 
    Classificado como peso normal

