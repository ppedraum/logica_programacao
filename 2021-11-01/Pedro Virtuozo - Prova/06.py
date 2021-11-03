candidatos=['Paulo', 'Pedro', 'José', 'Alfredo']
n_candidatos=[1, 2, 3, 4, 5, 6, 0]
escolhas=[]
cadastro=True

while cadastro:
    opc=int(input('Digite o número do candidato à sua escolha: \n(5=Voto Nulo, 6=Voto em branco)\n'))
    escolhas.append(opc)

    if(opc==0):
        cadastro=False        

print(f'Pedro: {escolhas.count(1)} votos')
print(f'Paulo: {escolhas.count(2)} votos')
print(f'José: {escolhas.count(3)} votos')
print(f'Alfredo: {escolhas.count(4)} votos')
print(f'Nulo: {escolhas.count(5)} votos')
print(f'Em branco: {escolhas.count(6)} votos')
