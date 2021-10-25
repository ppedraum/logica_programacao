n=[]
i=0

while True:
    n.append(int(input("Digite um número (digite 1000 para parar): ")))
    if(n[i]==1000):
        n.pop()
        break
    i+=1
print(f"Qtd nºs digitados: {len(n)}")
print(f"Soma dos nºs digitados: {sum(n)}")