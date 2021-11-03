cadastro=True
s_cadastro=""
nome=""
idade=0
peso=0
hr_sono=0
index=[]
ind_atrib=['idade', 'peso', 'horas de sono']


while cadastro:
    nome=input('Digite seu Nome: ')
    idade=int(input('Digite sua idade: '))
    if(idade<16)or(idade>69):
        index.append(0)
    else:
        index.append(1)
    peso=float(input('Digite seu peso: '))
    if(peso<50):
        index.append(0)
    else:
        index.append(1)
    
    hr_sono=float(input('Quantas horas você dormiu nas últimas 24 horas? '))
    if(hr_sono<6):
        index.append(0)
    else:
        index.append(1)
    if(sum(index)==3):
        print(f"Você, {nome}, pode doar sangue!")
    else:
        print("Você não pode doar sangue pois não atende os seguintes requisitos:\n")
        for i in range(len(index)):
            if(index[i]==0):
                print(ind_atrib[i])


    s_cadastro=int(input('Você deseja continuar o cadastro? \n1-Sim\n2-Não\n'))
    if s_cadastro==1:
        cadastro=True
    else:
        cadastro=False
