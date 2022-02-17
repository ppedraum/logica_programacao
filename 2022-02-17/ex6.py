"""
6) As maçãs custam R$ 1,30 cada se forem compradas menos de uma
dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um
programa que leia o número de maçãs compradas, calcule e escreva o
custo total da compra.
"""
preco_total=0
preco_un=0
n_macas=int(input("Digite o número de maçãs: "))
if n_macas>=12:
    preco_un=1
else:
    preco_un=1.5
preco_total=n_macas*preco_un
print(f"Preço para a compra de {n_macas} maçãs = R${preco_total} ({n_macas} * R${preco_un})")