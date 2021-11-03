import sys

nome=""
idade=0
salario=0
sexo=['feminino', 'masculino', 'outro']
s_sexo=''
est_civil=['solteiro', 'casado', 'viúvo', 'divorciado']
s_est_civil=''
cadastro=True
s_cadastro=""

while cadastro:
    nome=input('Digite seu Nome: ')
    if(len(nome)< 3):
        print('O nome precisa ter mais que 3 caracteres.')
    idade=int(input('Digite sua idade: '))
    if(idade<18)or(idade>110):
        print('Você precisa ter mais de 18 ou menos de 110 anos para se cadastrar. Sim, anciões não tem direitos nessa loja.')
    salario=float(input('Digite seu salário: '))
    if(salario<1045):
        print('Seu salário é muito baixo!')
    s_sexo=input('Digite seu Sexo: (masculino, feminino, outro)').lower()
    if s_sexo not in sexo:
        print("Você digitou seu sexo incorretamente.")
    s_est_civil=input('Digite seu estado civil: (solteiro, casaddo, viúvo, divorciado)')
    if s_est_civil not in est_civil:
        print('Você digitou seu estado civil incorretamente.')
    s_cadastro=int(input('Você deseja continuar o cadastro? \n1-Sim\n2-Não\n'))
    if s_cadastro==1:
        cadastro=True
    else:
        cadastro=False
