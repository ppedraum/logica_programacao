neg=[]
valores=[float(input(f'Digite o {i+1} valor: ')) for i in range(10)]
for i in range(len(valores)):
    if valores[i]<0:
        neg.append(valores[i])
print(f'valores negativos: {neg}')