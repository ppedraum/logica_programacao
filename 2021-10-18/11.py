sexo=""
isSexo=False

sexo=input("Digite seu sexo: ").upper()

while isSexo==False:
    if sexo=='M' or sexo=='F':
        print("OK")
        isSexo=True
    else:
        print("not OK")
        continue
print(f"Sexo validado! Seu sexo é {sexo}")