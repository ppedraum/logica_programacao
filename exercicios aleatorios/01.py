"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que 
a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de 
tinta a serem compradas e o preço total.
"""

cob_tinta=3
vol_tinta=18
preco_tinta=80.00
qtd_latas=0
nmr_larg=""
nmr_comp=""
unm_larg=""
unm_comp=""
area=0

un_medida=["cm","dm","m"]
valun_medida=[0.01, 0.1, 1]

larg=input("Digite a largura da parede (especifique a unidade de medida): ")
comp=input("Digite o comprimento da parede (especifique a unidade de medida): ")

for x in larg:
    if x.isdigit():
        nmr_larg=nmr_larg+x
    else:
        unm_larg=unm_larg+x.lower()

nmr_larg=float(nmr_larg)*valun_medida[un_medida.index(unm_larg)]

for x in comp:
    if x.isdigit():
        nmr_comp=nmr_comp+x
    else:
        unm_comp=unm_comp+x.lower()

nmr_comp=float(nmr_comp)*valun_medida[un_medida.index(unm_comp)]

area=nmr_larg*nmr_comp

qtd_latas=int(area/cob_tinta)+1
print(qtd_latas)



