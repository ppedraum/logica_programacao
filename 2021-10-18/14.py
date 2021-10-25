run=True
ctnRun=0
n=[]

while(run):
    ctnRun=0
    n.append(int(input("Digite um número: ")))
    while ctnRun==0:
        ctnRun=int(input("Você quer continuar escrevendo números?\n1-SIM\n2-NÃO\n\n"))
        if ctnRun==1:
            continue
        elif ctnRun==2:
            run=False
        else:
            print("Você digitou uma opção inválida!")
            ctnRun=0
print(f"Média dos números = {sum(n)/len(n)}")
print(f"Maior número = {max(n)}")
print(f"Menor número = {min(n)}")