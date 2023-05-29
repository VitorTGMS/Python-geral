n=int(input('Digite o numero de notas'))
soma=0
m=0
for i in range(0, n):
    num=int(input(f'Digite a {i+1} nota'))
    soma=soma+num

m=soma/n
print('A média é:', m)