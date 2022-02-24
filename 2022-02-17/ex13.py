""" 14) Ler dois valores e imprimir uma das três mensagens a seguir:
‘Números iguais’, caso os números sejam iguais
‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
‘Segundo maior’, caso o segundo seja maior que o primeiro. """

valores=[float(input(f'Digite o {i+1} valor: ')) for i in range(2)]
if valores[0]>valores[1]:
    print('Primeiro valor maior')
elif valores[0]<valores[1]:
    print('Segundo valor maior')
elif valores[0]==valores[1]:
    print('Valores iguais')
