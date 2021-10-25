primo=[2, 3, 5, 7, 11, 13, 17, 23, 27, 29, 31, 37, 41]
r=[]
q=[]
n = [int(input("Digite um Número para ver se é primo:"))]

for i in range(len(primo)):
    r.append(n%primo[i])
    q.append(n/primo[i])

    if r[i]==0 and n!=primo[i]:
        print("{} não é primo.".format(n))
        break
    elif r[i]!=0 and q[i]<primo[i]:
        print("{} é primo.".format(n))
        break
    else:
        continue
