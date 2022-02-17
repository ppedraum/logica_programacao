"""
5) Faça um algoritmo que leia três notas de um aluno, calcule e escreva a
média final deste aluno. Considerar que a média é ponderada e que o
peso das notas é 2, 3 e 5.
"""

notas=[]
pesos=[2,3,5]
media_final=0
for nota in range(3):
    notas.append(float(input(f"Digite sua {nota+1}ª nota: ")))
    media_final+=notas[nota]*pesos[nota]

media_final/=sum(pesos)


print("-"*30)
print("Sua média final = {:.2f}".format(media_final))