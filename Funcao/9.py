def reverso(n):
    rever=0
    while n>0:
        dig=n%10
        rever=(rever*10)+dig
        n=n//10
    print(f'O numero de digitos é: {rever}')

n=int(input('Digite um numero:'))

reverso(n)