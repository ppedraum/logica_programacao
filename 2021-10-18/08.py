ano=[]
maioridade=[]

for i in range(7):
    ano.append(int(input("Digite o ano de seu nascimento: ")))
    if(2021-ano[i]>=18):
        maioridade.append(True)
    else:
        maioridade.append(False)
print("Pessoas maiores de idade: {}".format(maioridade.count(True)))
print("Pessoas menores de idade: {}".format(maioridade.count(False)))

