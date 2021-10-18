
""" Em algumas situações é comum que uma mesma instrução (ou conjunto delas) 
precise ser executada várias vezes seguidas. Nesses casos, normalmente utilizamos um loop
(ou laço de repetição) que permite executar o mesmo bloco de código enquanto uma condição 
é atendida. Em Python, os loops são codificados com as estruturas de repetição for e while. """

""" A sintaxe do Python não possui a estrutura de repetição for tradicional, 
onde define-se uma variável, condição e incremento no cabeçalho da estrutura. A ideia, 
é o trabalho e manipulação de estrutura iteraveis, isto é, a definição de iteradores, ou melhor: 
objetos iteráveis - iterators. 
um objeto “iterável”, ele é qualquer tipo de coisa que você consegue realizar um laço sobre, 
por exemplo, um array, um objeto, uma sequencia de números, uma stream, ou qualquer coisa."""

""" A estrutura for exige, inicialmente, a definição de uma variável e, em seguida, a lista que será iterada. 
A seguir, temos o esquema para o uso da instrução for. """
'''for <variável> in <objeto iterável>:
    bloco de instrução'''

""" A variável a ser declarada na primeira parte da estrutura, receberá, a cada ciclo, 
um elemento contido na lista que está sendo iterada. Ao término, todos elementos terão sido percorridos 
e, a cada ciclo, o elemento seguinte contido no objeto iterável terá sido passado pela variável definida inicialmente. """

for item in [1, 2, 3, 4, 5]:
    print(item)

""" Nós podemos ler o laço de repetição definido acima for item in [1,2,3,4,5]: da seguinte maneira. 
Para cada elemento contido na lista [1,2,3,4,5] execute o bloco de código a seguir e a cada execução, 
atribua à variável item for item in um item da lista. """

lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item, '\n')

""" Ou entao, acima, definimos a variável item e uma lista com 5 elementos [1,2,3,4,5]. A cada ciclo, 
o elemento seguinte é atribuido à variável item e ao término, teremos executado um ciclo individual para 
cada elemento contido na lista. """

# USANDO A FUNÇÃO RANGE COM FOR:

""" A função range() retorna uma série numérica no intervalo enviado como argumento. """

""" sintaxe: """

# range (stop) # quando parar
# range (start, stop, steep) # steep é o intervalo de cada elemento


for item in range(2):
    print(item)

for item in range(3, 7):  # o ultimo do stop ele n entra
    print(item)
else:
    print("saiu do for!")  # da pra utilizar o else também

# steep 2 , significa que ele iré printar de 2 em 2.
for item in range(0, 20, 2):
    print(item)
print("saiu do for!")

for letras in "Linguagem Python!":  # percorre letra por letra
    print(letras)

# USANDO INPUT:
'''s = 0
for per in range(0,4): #o ultimo do stop ele n entra 
    n= int(input("Digite um valor: "))
    s = s + n 
    #s += n
    print("o somatório de todos os valores é:", s)
else:
    print ("saiu do for!")
 '''
s = 0
for per in range(0, 4):
    n = int(input("Digite um valor: "))
    s = s + n
    #s += n
print("o somatório de todos os valores é:", s)


num = 0
for num in range(10):
    if num == 5:
        break    # break aqui

    print('Número é ' + str(num))

print('Saiu do loop')

# Isso mostra que assim que o num é avaliado como equivalente a 5, o loop é interrompido, uma vez que o programa 
# é orientado a fazer isso com a instrução break. A instrução break faz com que um programa seja interrompido para fora de um loop.

#outro exemplo:

lista = [1,2,3,4,5,6,7,8,9,10]
for item in lista:
  if(item == 5):
    break
  else:
    print(item)

"""Aqui a lista vai imprimir até o número 4, depois disso entra no if do break e o loop é ejetado, é para isso que o break serve"""


num = 0

for num in range(10):
    if num == 5:
        continue    # continue aqui

    print('O número é ' + str(num))

print('Saiu do loop')

# A diferença entre usar a instrução continue, em vez de uma instrução break, é que o nosso código 
# continuará apesar da interrupção quando a variável num for avaliada como equivalente a 5.

# Você pode usar a instrução continue para evitar um código condicional extremamente aninhado, 
# ou para otimizar um loop, eliminando casos que ocorram com frequência e que você gostaria de rejeitar.

# A instrução continue faz com que um programa pule certos fatores que surjam dentro de um loop, 
# mas depois continuem pelo restante do loop.

#outro exemplo:
lista = [1,2,3,4,5,6,7,8,9,10]
for i in lista:
  if(i % 2 == 0):
    continue
  else:
    print(i)

#Aqui estamos dando continue nos valores pares da lista, então este exemplo só vai imprimir os valores ímpares

num = 0

for num in range(10):
    if num == 5:
        pass    # pass here

    print('O número é ' + str(num))

print('Saiu do loop')
# A instrução pass que ocorre após a instrução condicional if está dizendo ao programa para continuar executando o loop 
# e ignorar o fato de que a variável num é avaliada como equivalente a 5 durante uma das iterações.
# A instrução pass pode criar classes mínimas, ou agir como um espaço reservado enquanto estamos trabalhando em novos códigos 
# e pensando em um nível algorítmico antes de construir detalhes.

num = 4
if num > 5:
    pass

# o pass deve ser utilizado quando queremos que um código seja válido, mas ainda não pretendemos implementá-lo, Ou seja, 
# ele preenche um vazio e deixa o código ‘passar’.



***********************************************************************************************************************************************
#diferença: for vai executar as instruções através de uma sequência conhecida for  - percorrer listas, vetores, 
# executar um número definido x de ações e outros. Enquanto o while vai executar as instruções até que a(s) condição(ões) 
# seja(m) atendida(s) while .

#WHILE comparação com o for:

for i in range(1,10):  
    print(i)
print("Fim do nosso programa")

#usando while:
#quando eu não sei o limite não posso usar o for, agora quando sabemos o limite não importa qual dos dois usar
i = 1
while i < 10:
    print(i)
    i +=1
print("Fim do nosso programa")

#outro exemplo:
#ou seja, eu sei o valor, ele inicia em 1 e termina em 4 , eu sei o limite
for i in range (1,5): 
    n = int(input("Digite um valor: "))
print("Fim do nosso programa")


#não tem um limite, e sim uma condição de parada, que seria quando for digitado o valor 0 o programa para
i = 1
while i != 0:
    n = int(input("Digite um valor: "))
print("Fim do nosso programa")

### posso criar qualquer situação.
resp = "S"
while resp =="S":
    n = int(input("Digite um valor: "))
    resp = input("Deseja continuar? [S/N] ").upper()
print("Fim do nosso programa")

#exemplos: for:

#while :


#enquanto não for 0 ele continua rodando o programa .

num = 1 
par = 0
impar = 0 
# ou par=impar=0 
while num != 0:
    num = int(input("Digite um valor: "))
    if num != 0:
        if num % 2== 0:
            par += 1
        else:
            impar +=1
print("Foram digitados {} numero pares e {} numeros impares.".format(par, impar))

#COMO ARRUMAR?

num = 1 
par = 0
impar = 0 

while True:
    num = int(input("Digite um valor: "))
    if num ==0:
        break
    if num % 2== 0:
        par += 1
    else:
        impar +=1
            
print('Foram digitados {} numero pares e {} numeros impares.'.format(par, impar))


#FUNÇÃO RANDOM 
#random.randint(a, b)
#Retorna um inteiro aleatório N de forma que a <= N <= b. Apelido para randrange(a, b+1).

from random import randint

num = randint(1,11)
print(num)
