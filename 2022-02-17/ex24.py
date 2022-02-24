'''BOMBA DE COMBUSTIVEL'''

class combustivel:

    def __init__(self, iPreco, iTipoDsct):
        self.preco=iPreco
        self.tipoDsct=iTipoDsct

def dsct_tipo(combustivel, tipo, qtd):
    return round(combustivel.preco*combustivel.tipoDsct[0]*qtd, 2)

etn=combustivel(3.3, [0.03, 0.05])
gas=combustivel(2.9, [0.4, 0.6])


qtd=float(input('Digite a quantidade de combustível: '))

print(dsct_tipo(etn, 0, 10))


'''Em andamento'''