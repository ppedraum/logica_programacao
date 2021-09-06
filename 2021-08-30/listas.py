""" lista = ["maçã", "banana", "melancia", "jujuba"]
print(lista[0]) #informação na pos. 0
print(lista[0:3]) #intervalo de posições
lista.insert(1, "goiaba") #inserir na posição
lista.append("pera") #adicionar à lista
print(lista.index("jujuba")) #mostra a posição da informação
print(lista) 
del lista[1] #deleta a informação na pos. específica
print(lista)
lista.remove("jujuba") # remove a informação
print(lista)
lista.pop(0) #oculta a informação
print(lista)
#lista.clear(); #limpa a lista, mas não destrói a variável
print(lista)
lista_nova = lista.copy() #copia a lista para uma nova
print(lista_nova)
print(lista.count("banana")) #conta a quantidade de vezes que aparece tal informação
lista.append("abacate")
print(lista)
print(sorted(lista)) #arranja de forma alfabética as informações """

'''
1. Escreva um Programa que leia uma lista de 5 números inteiros e mostre-os.
2. Escreva um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.
3. Escreva um Programa que leia 4 notas, mostre as notas e a média na tela.
4. Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles.
5. Escreva um Programa que verifique se um elemento está na lista.
6. Escreve um Programa que verifque a posição exata de um elemento da lista.
7. Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e
mostre os itens repetidos. 
'''

""" #1
numeros = [1, 2, 3, 4, 5]
print("#1: ", numeros)
#2
numeros = [1, 2, 3, 4, 5, 1.5, 2.5, 3.5, 4.5, 5.5]
numeros.sort()
numeros.reverse()
print("#2: ", numeros)
#3
nota1 = float(input("Digite a 1ª nota"))
nota2 = float(input("Digite a 2ª nota"))
nota3 = float(input("Digite a 3ª nota"))
nota4 = float(input("Digite a 4ª nota"))
notas = [nota1, nota2, nota3, nota4]
media = sum(notas)/len(notas)
print("#3: Notas ->", notas)
print("Média -> ", media) """
#4
n1 = float(input("Digite o 1ª numero"))
n2 = float(input("Digite o 2ª numero"))
n3 = float(input("Digite o 3ª numero"))
n4 = float(input("Digite o 4ª numero"))
n5 = float(input("Digite o 5ª numero"))


