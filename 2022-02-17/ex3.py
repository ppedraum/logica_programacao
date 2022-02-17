"""
3) O custo de um carro novo ao consumidor é a soma do custo de fábrica
com a porcentagem do distribuidor e dos impostos (aplicados ao custo de
fábrica). Supondo que o percentual do distribuidor seja de 28% e os
impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um
carro, calcular e escrever o custo final ao consumidor.

"""
pct_dist=0.28
pct_imp=0.45
c_fabrica=0
c_total=c_fabrica+(c_fabrica*pct_dist)+(c_fabrica*pct_imp)


c_fabrica=float(input("Digite o custo de fábrica do veículo: R$"))
print("")
print("-"*30)
c_total=c_fabrica+(c_fabrica*pct_dist)+(c_fabrica*pct_imp)
print("Custo final = R${:.2f}".format(c_total))
print("-"*30)
