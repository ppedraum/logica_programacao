""" 15) Escreva um algoritmo para ler 2 valores e se o segundo valor
informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo  """

valor1=float(input('Digite o 1 valor: '))


for i in range(10000000):
    valor2=float(input('Digite o segundo valor: '))
    if(valor2==0):
        print('O segundo valor n pode ser 0!')
    else:
        break

print('{:.2f} : {:.2f} = {:.2f}'.format(valor1, valor2, valor1/valor2))
    
