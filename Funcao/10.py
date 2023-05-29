import random

def primeiro (d):
    if d==7 or d==11:
        print('Natural, ganhou')
        return 20
    elif d==2 or d==3 or d==12:
        print('Craps, perdeu')
        return 20
    else:
        print(f'Seu ponto é: {d}')
        p=d
        return p

def ponto (d, p):
    if d==7:
        print('perdeu')
        return 20
    elif d==p:
        print('ganhou')
        return 20
    else:
        print('Jogue novamente')

i=0
while True:
    r=input('Deseja jogar?')
    r=r.upper()
    if r!='S':
        break
    d=random.randrange(1,12)
    i=i+1
    if i==1:
        p=primeiro(d)
        if p==20:
            break
    else:
        res=ponto(d, p)
        if res==20:
            break
    