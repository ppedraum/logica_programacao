'''
1) Faça um programa que mostre a possibilidade de uma criança do sexo masculino nascer com paralisia cerebral. 
O índice da doença é de 2/1000 nascidos vivos, sendo que a probabilidade da criança nascer menino é de 50%.
'''

prb_paralisia=1/500
prb_sexo=1/2

print("A probabilidade de um menino nascer com paralisia é: {:.1f}%".format(prb_paralisia*prb_sexo*100))