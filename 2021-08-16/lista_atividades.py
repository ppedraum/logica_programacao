""" #1
n = input("Digite um número inteiro: ")

if n.isnumeric():
    n = int(n)
    print("Seu número é {}.".format(n))
else:
    print("Você não digitou o número inteiro corretamente!")"""

""" #2
def is_number(s): #criando uma função para validar um número tipo float (não sei como fazer, peguei da internet)
    try:
        float(s)
        return True
    except ValueError:
        return False
#fonte: https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float

n = input("Digite um número real: ")

if (is_number(n)):
    n = float(n)
    print("Seu número é {:.2f}.".format(n))
else:
    print("Você não digitou o número real corretamente!") """

""" #3
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = int(input("Digite outro número inteiro: "))

print("A soma de {}, {} e {} é {:-^11}.".format(n1, n2, n3, n1+n2+n3)) """

""" #4
n = int(input("Digite um número inteiro: "))
print("O quadrado desse número é {}.".format(n**2)) """

""" #5
n = int(input("Digite um número inteiro: "))
print("A quinta parte desse número é {}.".format(n/5)) """

""" #6
c = float(input("Digite uma temperatura em celcius: "))
f = c*(9/5) + 32
print("f = {}*(9/5) + 32 ----> f = {} ºF".format(c, f) ) """

""" #7
f= float(input("Digite uma temperatura em farenheit: "))
c = 5*(f - 32)/9 
print("c = 5*({} - 32)/9 ----> c = {:.2f} ºC".format(f, c) ) """

""" #8
k = float(input("Digite uma temperatura em kelvin: "))
c = k - 273.15
print("c = k - 273.15 ----> c = {:.2f} ºC".format(c)) """

""" #9
c = float(input("Digite uma temperatura em celcius: "))
k = c + 273.15
print("k = c + 273.15 ----> k = {:.2f} K".format(k) ) """