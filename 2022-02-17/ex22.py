""" 22) Ler 10 valores e escrever quantos desses valores lidos estão no
intervalo [10,20] (incluindo os valores 10 e 20 no intervalo) e quantos
deles estão fora deste intervalo. """
inrange=[]
valores=[float(input(f'Digite o {i+1} valor: ')) for i in range(10)]

for i in range(len(valores)):
    if valores[i] in range(10,21):
        inrange.append(valores[i])
print(f'valores entre 10 e 20: {inrange}')