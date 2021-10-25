nome=[]
idade=[]
sexo=[]

for i in range(4):
    nome.append(input("Digite seu Nome: "))
    idade.append(int(input("Digite sua Idade: ")))
    sexo.append(input("Digite seu Sexo: "))

print("A média de idade de todos é: {}".format(sum(idade)/len(idade)))
print("O Homem mais velho é: ", nome[idade.index(max(idade))])