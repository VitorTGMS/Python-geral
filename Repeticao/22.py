n=int(input('Digite um numero'))
d=0

for i in range(n-1, 1, -1):
    if n%i==0:
        d=d+1
        print(f'O numero e divisível por {i}')
if d==0:
    print('O número é primo')