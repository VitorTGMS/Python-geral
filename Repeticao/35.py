n=int(input('Digite um número qualquer'))
d=0

for i in range(1, n):
    for j in range(2, i):
        if i%j==0:
            d=d+1
    if d==0:
        print(i, end=' ')
    d=0