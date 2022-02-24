""" 17) Escreva um algoritmo para ler as notas da 1a. e 2a. avaliações de um
aluno, calcule e imprima a média (simples) desse aluno. Só devem ser
aceitos valores válidos durante a leitura (0 a 10) para cada nota. """

""" 18) Acrescente uma mensagem 'NOVO CÁLCULO (S/N)?' ao final do
exercício [17]. Se for respondido 'S' deve retornar e executar um novo
cálculo, caso contrário deverá encerrar o algoritmo. """

while True:
    valor1=float(input('Digite o primeiro valor: '))
    valor2=float(input('Digite o primeiro valor: '))
    if(valor2<0 or valor2>10 or valor1<0 or valor1>10):
        print('Digite valores válidos!')
    else:
        print('({:.2f} + {:.2f})/2 = {:.2f}'.format(valor1, valor2, (valor1+valor2)/2))
        novo_c=input('Novo cálculo? S/N: ').lower()
        if(novo_c=='s'):
            pass
        else:
            break

