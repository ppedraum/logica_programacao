""" 27) Uma empresa quer verificar se um empregado está qualificado para a
aposentadoria ou não. Para
estar em condições, um dos seguintes requisitos deve ser satisfeito:
- Ter no mínimo 65 anos de idade.
- Ter trabalhado no mínimo 30 anos.
- Ter no mínimo 60 anos e ter trabalhado no mínimo 25 anos.
Com base nas informações acima, faça um algoritmo que leia: o número
do empregado (código), o ano
de seu nascimento e o ano de seu ingresso na empresa. O programa
deverá escrever a idade e o tempo
de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou
'Não requerer'. """

req_apos=False
codigo=0
ano_nasc=0
ano_entr=0

def idade():
    return 2022-ano_nasc
def t_trabalho():
    return 2022-ano_entr

codigo=int(input('Digite seu código: '))
ano_nasc=int(input('Digite o ano de seu nascimento: '))
ano_entr=int(input('Digite o ano de entrada na empresa: '))
if(idade()>=65): req_apos=True
elif(t_trabalho()>=30): req_apos=True
elif(idade()>=60 and t_trabalho()>=25): req_apos=True
elif(idade()>=60 and t_trabalho()>=25): req_apos=True
else: req_apos=False

print(f'Idade: {idade()}')
print(f'Tempo de trabalho: {t_trabalho()}')
print('Requerer aposentadoria: {}'.format('requerer' if req_apos==True else 'Não Requerer'))
