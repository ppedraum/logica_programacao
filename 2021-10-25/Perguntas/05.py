'''5)faça um programa que simule um jogo onde você tem que andar pra alguma direção, e lá acontecerá alguma coisa.'''

print("Você acorda no meio do nada, na sua mão há uma espada e à sua frente, 3 caminhos diferentes para seguir.")
print('e)ESQUERDA f)PARA FRENTE d)PARA A DIREITA ')
drc=input("Digite para onde você quer ir:")

if drc=='e':
    print('-------------------------------------------------')
    print("Você cai em um poço de lava e morre. \nFIM DO JOGO")
    print('-------------------------------------------------')
elif drc=='c':
    print('-------------------------------------------------')
    print("Você encontra uma gosma viva! Você a mata com sua espada. \nFIM DO JOGO")
    print('-------------------------------------------------')
elif drc=='d':
    print('-------------------------------------------------')
    print("Você entra num castelo, mata um dragão/tartaruga cuspidor de fogo, \nsó para ser notificado por um cogumelo ", end='')
    print("que a princesa está em outro castelo. \nFIM DO JOGO")
    print('-------------------------------------------------')