""" 4) Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada, utilizando o laço for.
 """
n=int(input("Digite um número: "))
resultado="TABUADA DE {}: \n".format(n)

for i in range(10):
     resultado+="\n {}x{}={}".format(n,i+1,n*(i+1))
print(resultado)