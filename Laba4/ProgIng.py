studen=['Vasa', 'Irina', 'Feda', 'Kata']
men=['Vasa', 'Feda']
women=['Irina', 'Kata']
otlichnic=['Kata']
horoshist=['Feda', 'Irina']
troechnic=['Vasa']
molodci=[]
for i in range(len(otlichnic)):
    molodci.append(otlichnic[i])
for i in range(len(horoshist)):
    molodci.append(horoshist[i])
print("Молодцы:")
for i in range(len(molodci)):
    print(molodci[i])
otvet=[]
for i in range(len(men)):
    for j in range(len(molodci)):
        if men[i]==molodci[j]:
            otvet.append(men[i])
if len(otvet)>0:
    print('\n\t', 'Yes')
    for i in range(len(otvet)):
        print('\t', otvet[i])
else: print('\n\tNo')