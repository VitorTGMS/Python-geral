r=input('Deseja começar um novo fatorial S ou N?')
r=r.upper()
while r=='S':
    n=float(input('Digite um numero'))
    m=n.is_integer()
    f=n
    if n < 0 or n > 16 or n//1!=n:
        print('Valor invalido')
    else:
        for i in range(1,m):
            f=f*i
        print(f)
    r=input('Deseja começar um novo fatorial S ou N?')
    r=r.upper()