valor1=float(input('Digite o primeiro valor: '))

while True:
    valor2=float(input('Digite o primeiro valor: '))
    if(valor2==0):
        print('O segundo valor n pode ser 0!')
    else:
        break

print('{:.2f} : {:.2f} = {:.2f}'.format(valor1, valor2, valor1/valor2))