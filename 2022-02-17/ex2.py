""" 
2) Escreva um algoritmo para ler o número total de eleitores de um
município, o número de votos brancos, nulos e válidos. Calcular e escrever
o percentual que cada um representa em relação ao total de eleitores.  
"""

eleitores=int(input("Digite a qtd de eleitores: "))
v_branco=0
v_nulos=0
v_validos=0
for i in range(eleitores):
    print("-----------------------------")
    print("1-Voto em branco")
    print("2-Voto nulo")
    print("3-Voto normal")
    voto=int(input("Digite o seu voto: "))
    print("-----------------------------")
    print("")

    if voto==1:
        v_branco+=1
    elif voto==2:
        v_nulos+=1
    elif voto==3:
        v_validos+=1
    else:
        print("Você não digitou corretamente.")
        break


pct_validos=(v_validos*100)/eleitores
pct_nulos=(v_nulos*100)/eleitores
pct_branco=(v_branco*100)/eleitores

print("-----------------------------")
print("Eleições 2022")
print("")
print(f"Número de Eleitores: {eleitores}")
print("Número de votos nulos: {} ({:.2f}%)".format(v_nulos, pct_nulos))
print("Número de votos em branco: {} ({:.2f}%)".format(v_branco, pct_branco))
print("Número de votos válidos: {} ({:.2f}%)".format(v_validos, pct_validos))
print("")
print("-----------------------------")