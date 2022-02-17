"""
7) Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média
aritmética simples e escrever uma mensagem que diga se o aluno foi ou
não aprovado (considerar que nota igual ou maior que 6 o aluno é
aprovado). Escrever também a média calculada.
"""

notas=[]
media=0
situacao='reprovado'

for nota in range(2):
    notas.append(float(input("Digite sua {}ª nota: ".format(nota+1))))

media=sum(notas)/len(notas)
if media>=6:
    situacao='aprovado'

print('-'*30)
print("BOLETIM")
print("")
for i in notas:
    print("NOTA {}: {}".format(notas.index(i)+1, i))
print("")
print("MEDIA FINAL: {:.2f}".format(media))
print(f"SITUAÇÃO: {situacao}")
print("")
print('-'*30)
