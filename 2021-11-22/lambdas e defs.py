#1
""" def qtd_digitos(string):
    chars= len(string)
    return chars

print(qtd_digitos('wfgrwegeg'))
 """

#2
""" def despotencializador(num):
    for n in range(100):
        for p in range(100):
            if(n**p==num):
                print(f'{n}**{p}')
            else:
                continue
 """

#3
""" def datamaker(data):
    values=['0','0','0']
    tipo=0
    for i in data:
        if i == "/":
            tipo+=1
        if tipo>2: break
        if i.isnumeric():
            values[tipo]+=str(i)
    return int(values[0]), int(values[1]), int(values[2])

def voto(nasc):
    est_voto=''
    if 2021-datamaker(nasc)[2]>18:
        est_voto="Voto obrigatório"
    elif 2021-datamaker(nasc)[2]<18 and 2021-datamaker(nasc)[2]>15:
        est_voto="Voto opcional"
    else:
        est_voto="Voto negado"
    return est_voto
print(voto(input("digite sua data de nascimento: "))) """

#4
jogadores=[]
def ficha(nome='Anderson', gols=0):
    jogadores.append([nome, gols])
