""" 6) Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre 
os 10 primeiros termos dessa progressão """

xO=0
termos=[]
r=int(input("Digite a razão da P.A.: "))
x=int(input("Digite o primeiro termo da P.A.: "))

for i in range(10):
    xO=x+r
    termos.append(xO)
    x=xO
print("10 PRIMEIROS TERMOS DA P.A.: ",termos)