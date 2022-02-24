""" 25) Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres
(considere que as idades dos homens serão sempre diferentes entre si,
bem como as das mulheres). Calcule e escreva a soma das idades do
homem mais velho com a mulher mais nova, e o produto das idades do
homem mais novo com a mulher mais velha. """

age_man=[float(input(f'Digite a {i+1} idade (homem): ')) for i in range(2)]
age_wman=[float(input(f'Digite a {i+1} idade (mulher): ')) for i in range(2)]

soma=max(age_man)+min(age_wman)
produto=min(age_man)*max(age_wman)

print('SOMA={:.2f} PRODUTO ={:.2f}'.format(soma, produto))