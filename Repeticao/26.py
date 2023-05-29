n=int(input('Digite o numero de eleitores'))
a=0
b=0
c=0
d=0
print('Digite seu voto')
print('Digite "A" para votar em A')
print('Digite "B" para votar em B')
print('Digite "C" para votar em C')
for i in range(0, n):
    vot=input()
    vot=vot.upper()
    
    if vot=='A':
        a=a+1
    elif vot=='B':
        b=b+1
    elif vot=='C':
        c=c+1
    else:
        d=d+1
print(f'O candidato "A" teve {a} votos')
print(f'O candidato "B" teve {b} votos')
print(f'O candidato "C" teve {c} votos')
print(f'ouve {d} votos brancos ou nulos')