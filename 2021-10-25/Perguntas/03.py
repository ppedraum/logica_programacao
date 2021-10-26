'''4) faça um programa que leia 2 dias setembro e indique o tempo, em dias, entre cada um deles.'''

setembro=[]
for i in range(1, 31):
    setembro.append(i) #colocando os dias em uma lista

dia=[]
dia.append(int(input("Digite um dia de setembro: ")))
dia.append(int(input("Digite outro dia de setembro: "))) #os dias que vão ser o intervalo

intervalo=setembro[dia[0]:dia[1]-1] #nova lista com o intervalo entre os dois dias

print("O intervalo entre os dias {} e {} de setembro é: {} dias ({})".format(dia[0], dia[1], len(intervalo), intervalo)) 
#printar o número de dias e os dias que estão entre eles