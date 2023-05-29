num=[]
par=[]
impar=[]

for i in range(0, 20):
    n=int(input('Digite um número inteiro'))
    num.append(n)
    
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)

print('Os números digitados foram:\n')
for i, n in enumerate(num):
    print(n)


print('O números pares digitados foram:\n')
for i, n in enumerate(par):
    print(n)

print('Os números inpares digitados foram:\n')
for i, n in enumerate(impar):
    print(n)