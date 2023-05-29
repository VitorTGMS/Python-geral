n=int(input('Digite um número inteiro diferente de 0'))
print('S=1/1', end='+')
S=1
m=3
for i in range(2,n):
    print(f'{i}/{m}', end='+')
    S=S+i/m
    m=m+2
print(f'{n}/{m}')
S=S+n/m
S=round(S,2)
print(f'S={S}')