def digitos(n):
    i=0
    while n>0:
        i=i+1
        n=n//10
    print(f'O numero de digitos é: {i}')

n=int(input('Digite um numero:'))

digitos(n)