import sys

valor=[]
resultado=0
opcoes=['SOMA', 'MULTIPLICAÇÃO', 'Nº MAIOR', 'Nº MENOR']
valor.append(float(input("Digite um Valor: ")))
valor.append(float(input("Digite outro Valor: ")))

while True:
    opt=int(input("1-Soma \n2-Multiplicação \n3-Nº maior \n4-Nº menor \n5-Sair do programa \n\nDigite a operação desejada: "))
    if opt==1:
        resultado=valor[0]+valor[1]
        break
    elif opt==2:
        resultado=valor[0]*valor[1]
        break
    elif opt==3:
        if(valor[0]>valor[1]):
            resultado=valor[0]
        else:
            resultado=valor[1]
        break
    elif opt==4:
        if(valor[0]<valor[1]):
            resultado=valor[0]
        else:
            resultado=valor[1]
        break
    elif opt==5:
        print("Saindo do programa!")
        sys.exit()
    else:
        print("Você digitou uma opção inválida! \n\nTente Novamente:\n")

print(f"Resultado: {opcoes[opt-1]} = {resultado}")


