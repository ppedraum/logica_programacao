ano_atual=int(input("Digite o ano atual"))
ano_nasc=int(input("digite o ano de seu nascimento"))

if ano_atual-ano_nasc >=16:
    print('pode votar')
else:
    print('Não pode votar')