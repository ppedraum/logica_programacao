""" 5) Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
Se o valor digitado for ímpar desconsidere-o.
 """
n=[]
soma=0
for i in range(6):
    n.append(int(input("Digite um número: ")))

for j in n:
    if(j%2==1):
        continue
    else:
        soma+=j
print("SOMA TOTAL DOS NÚMEROS ÍMPARES EM {}: {}".format(n, soma))