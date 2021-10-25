import random
import sys

choice=0
n_player=0
n_machine=0
result=""

choice=int(input("Vamos jogar par ou ímpar!\nPrimeiro, escolha:\n1-ÍMPAR\n2-PAR\n\n"))

n_player=int(input("Digite seu número.\n"))

if choice==1:
    n_machine=random.randrange(1, 10001)

if choice==2:
    n_machine=random.randrange(1, 10001, 2)

if n_player%2==choice-1:
    print("Você trapaceou.")
    sys.exit()

if (n_player+n_machine)%2==choice-1:
    print(f"Você perdeu. (Número do oponente = {n_machine}, seu número = {n_player}, soma = {n_player+n_machine})")
    sys.exit()
else:
    print(f"Você ganhou. (Número do oponente = {n_machine}, seu número = {n_player})")
    sys.exit()


