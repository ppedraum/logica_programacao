par=0
impar=0
n=0
resp=""

while resp != "N":
    i=int(input("digite um número: "))
    if i % 2 == 0:
        par+=1
    else:
        impar+=1
    resp=input("Deseja continuar? (S/N): ").upper()
print("Quantidade de números pares: ", par)
print("Quantidade de números ímpares: ", impar)

