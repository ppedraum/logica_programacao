lista = ["maçã", "banana", "melancia", "jujuba"]
print(lista[0])
print(lista[0:3])
lista.insert(1, "goiaba")
lista.append("pera")
print(lista.index("jujuba"))
print(lista)
del lista[1]
print(lista)
lista.remove("jujuba")
print(lista)
lista.pop(0)
print(lista)