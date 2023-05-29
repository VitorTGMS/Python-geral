n=int(input('Digite um número inteiro diferente de 0'))
S=0
print('H',end='=')
for i in range(1,n):
    print(f'1/{i}', end='+')
    S=S+1/i
print(f'1/{n}')
print(f'H={S:.2f}')