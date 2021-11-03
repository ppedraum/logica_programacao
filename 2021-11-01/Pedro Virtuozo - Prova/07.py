compra=True
programa=True
produto=0
val_produtos=[]
val_total=0
val_recebido=0
troco=0
while programa:
    while compra:
        produto+=1
        val=float(input(f'Digite o valor do produto {produto}: '))
        val_produtos.append(val)

        if(val==0):
            compra=False
    for i in range(len(val_produtos)):
        print('Produto {} = R${:.2f}'.format(i+1, val_produtos[i]))
    val_total=sum(val_produtos)
    print("Valor Total: R${:.2f}".format(val_total))
    val_recebido=float(input('Digite o valor recebido como pagamento: '))
    troco=val_recebido-val_total
    if(troco<0):
        print('O cliente forneceu menos dinheiro que o valor total das compras.')
    else:
        print("Troco: R${:.2f}".format(troco))