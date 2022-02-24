""" 23) Escreva um algoritmo para ler 8 números. Todos os números lidos com
valor inferior a 40 devem ser somados. Escreva o valor final da soma
efetuada. """

inrange=0
valores=[float(input(f'Digite o {i+1} valor: ')) for i in range(8)]

for i in range(len(valores)):
    if valores[i] < 40:
        inrange+=valores[i]
print(f'soma de valores menores que 40: {inrange}')