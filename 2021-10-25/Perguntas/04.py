'''4) Faça um programa que some o número dos códigos das letras de uma frase (padrão ASCII)'''

frase=input("Digite uma frase: ")
sum_ascii=0

for i in frase: #letra por letra da frase
    sum_ascii+=ord(i) #transforma uma letra em um código ascii
print(f"Uma soma muito doida é igual a {sum_ascii}")
