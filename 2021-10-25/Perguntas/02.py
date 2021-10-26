'''2) Faça um programa que leia 3 números e diga se algum desses pertence à sequência de fibonacci (e quantos). 
A fórmula para a sequência de fibonacci é fn[i] = fn[i-1]+fn[i-2], sendo que ela começa com 0 e 1, respectivamente.'''

fn=[0,1]
for i in range(2, 99): #pegar os 100 primeiros itens da sequência de fibonacci
    fn.append(fn[i-1]+fn[i-2]) 

n=[]

print("Digite 3 números para o verificador da sequência de fibonacci:")
for i in range(3):
    n.append(int(input()))

inn_join=[]
for i in range(len(fn)):#verifica 1 por 1 na lista da sequência e salva em inn_join se os numeros digitados aparecerem
    if fn[i] in n and inn_join.count(fn[i])<2:     
        inn_join.append(fn[i])
    else:
        continue
inn_join.remove(1)#O 1 aparece 2 vezes por padrão na sequência, então para evitar que apareça repetido na lista da intersecção, remove 1 "1"

print(f"Há {len(inn_join)} números que fazem parte da sequência, respectivamente: {inn_join}")#printa os números que apareceram
