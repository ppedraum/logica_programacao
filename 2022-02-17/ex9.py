""" ) Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma
empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total
das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor,
calcular e escrever o seu salário total """
pgto=0
sal=float(input('Digite valor'))
if sal>1500:
    pgto+=(sal-1500)*0.05 + 1500*0.03
else:
    pgto+=sal*0.03
print(pgto)