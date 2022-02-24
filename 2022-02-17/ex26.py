notas=[]
pesos=[1,2,3,1]
media_final=0
conceito=''
for nota in range(3):
    notas.append(float(input(f"Digite sua {nota+1}ª nota: ")))
    media_final+=notas[nota]*pesos[nota]
media_final+=float(input('Agora digite a média de suas 3 avaliações: ')*pesos[3])
media_final/=sum(pesos)
if media_final>=9: conceito='A'
elif media_final<9 and media_final>=7.5: conceito='B'
elif media_final<9 and media_final>=7.5: conceito='B'
elif media_final<7.5 and media_final>=6: conceito='C'
elif media_final<6: conceito='D'

print('media final={}  conceito={}'.format(round(media_final,2), conceito))