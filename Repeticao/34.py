from sys import exit
n=int(input('Digite um número qualquer:'))

for i in range(2, n):
    if n%i==0:
        print('O numero não é primo')
        exit()