#!/usr/bin/env python
# coding: utf-8

# In[6]:


n = []
n.append(float(input("Digite um número: ")))
n.append(float(input("Digite outro número: ")))
print("O maior número é:", max(n))


# In[13]:


n = float(input("Digite um número: "))
if(n>0):
    print("O número é positivo!")
elif(n<0):
    print("O número é negativo!")
else:
    print("O número é 0!")


# In[16]:


letra = input("Digite seu sexo: \nM - Masculino \nF - Feminino \n")
print("--------------------")
if(letra == 'M'):
    print("Masculino")
elif(letra == 'F'):
    print("Feminino")
else:
    print("Sexo Inválido!")


# In[18]:


idade = int(input("Digite sua idade: "))

if(idade >= 18):
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")


# In[29]:


resposta = input("A África Subsaariana é localizada: \nA)Ao norte \nB)Ao sul \nC)Ao leste \nD)Ao oeste \n \nDigite a letra correta: ").upper()
if(resposta == 'B'):
    print("Resposta correta!")
elif(resposta == 'A')or(resposta == 'C')or(resposta == 'D'):
    print("Resposta errada!")
else:
    print("Resposta inválida!")


# In[32]:


nome = input("Digite um nome: ").lower();
r = input("Você gosta desse nome? ")
if(r == "não"):
    print("Que pena :-(")
elif(r == "sim"):
    print("Legal ^^")
else:
    print("Não entendi o que você falou >< tente novamente!")


# In[42]:


r_irmao = input("Você tem algum irmão?").lower()
if(r_irmao == "sim"):
    r_nirmaos = int(input("Quantos irmãos você tem?"))
    lista_irmaos = []
    for i in range(r_nirmaos):
        lista_irmaos.append(input("Digite o nome do seu {}º irmão: ".format(i+1)))
    print("Sua lista de irmãos: ", lista_irmaos)
elif(r_irmao == "não"):
    r_wantirmao = input("Você gostaria de ter algum irmão?").lower()
    if(r_wantirmao == "sim"):
        print("Legal!")
    elif(r_wantirmao == "não"):
        print("Massa!")
    else:
        print("RESPOSTA INVÁLIDA POR FAVOR TENTE NOVAMENTE")
else:
    print("RESPOSTA INVÁLIDA POR FAVOR TENTE NOVAMENTE")
    


# In[45]:


bebidas = ["capirinha", "coca-cola", "suco"]
bebida = int(input("1-{}\n2-{}\n3-{}\n \nDigite uma bebida:".format(bebidas[0], bebidas[1], bebidas[2])))
print(bebidas[bebida-1])


# In[47]:


n = []
n.append(float(input("Digite um número: ")))
n.append(float(input("Digite outro número: ")))
if n[0] == n[1]:
    print("Os dois números são iguais!")
else:
    print("O maior número é:", max(n))


# In[49]:


n = []
n.append(float(input("Digite um número: ")))
n.append(float(input("Digite outro número: ")))
operacao = int(input("Você deseja fazer \n1-Adição \n2-Subtração \n"))
if(operacao == 1):
    print("{}-{}={}".format(n[0], n[1], n[0]+n[1]))
elif(operacao == 2):
    print("{}-{}={}".format(n[0], n[1], n[0]-n[1]))
else:
    print("Você não escolheu certo! tente novamente.")


# In[50]:


n = []
n.append(float(input("Digite um número: ")))
n.append(float(input("Digite outro número: ")))
operacao = int(input("Você deseja fazer \n1-Multiplicação \n2-Divisão \n"))
if(operacao == 1):
    print("{}*{}={}".format(n[0], n[1], n[0]*n[1]))
elif(operacao == 2):
    print("{}/{}={}".format(n[0], n[1], n[0]/n[1]))
else:
    print("Você não escolheu certo! tente novamente.")


# In[53]:


temperatura = float(input("Digite uma temperatura: "))
if(temperatura < 20):
    print("Frio")
if(temperatura > 30):
    print("Quente")
if(temperatura > 22)and(temperatura<25):
    print("Agradável")


# In[54]:


conversao = int(input("Você deseja fazer a conversão: \n1-celcius/farenheit \n2-farenheit/celcius \n"))
if(conversao == 1):
    c = float(input("Digite uma temperatura em celcius: "))
    f = c*(9/5) + 32
    print("f = {}*(9/5) + 32 ----> f = {} ºF".format(c, f)) 
elif(conversao == 2):
    f= float(input("Digite uma temperatura em farenheit: "))
    c = 5*(f - 32)/9 
    print("c = 5*({} - 32)/9 ----> c = {:.2f} ºC".format(f, c) )
else:
    print("Você não escolheu certo! tente novamente.")


# In[ ]:


peso = float(input("Digite a merda do seu peso seu filho da puta"))
sexo = int(input("Agora digita a merda do seu sexo seu filho da puta"))
h = float(input("Digite a merda do seu altura seu filho da puta"))
if(sexo == 1):
    print("Peso ideal fodase: {}".format((72.7*h) - 58))
elif(sexo == 2):
    print("Peso ideal fodase: {}".format((62, 1*h) - 44,7))


# In[ ]:




