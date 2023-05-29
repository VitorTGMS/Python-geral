n=int(input('Digite um número'))
f=1
for i in range(n, 0, -1):
    f=f*i

print(f'O fatorial do número {n} é {f}')