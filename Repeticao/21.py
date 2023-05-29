n=int(input('Digite um numero'))
d=0
for i in range(2, n):
    if n%i==0:
        print('O número não é primo')
        d=d+1
        break

if d==0:
    print('O número é primo')