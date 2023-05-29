nota=[]
n=0
while True:
    n=float(input('Digite a sua nota'))
    if n==-1:
        break
    nota.append(n)

print(f'O número de notas armazenadas foi {len(nota)}')

for i in nota:
    print(i, end=' ')
print('\n')
nota.reverse()

for i in nota:
    print(i)

print(f'A soma das notas é {sum(nota)}')

m=sum(nota)/len(nota)
print(f'A média das notas é: {m}')

for i in nota:
    if i >=m:
        n+=1
print(f'A quantidade de notas acima da média é: {n}')
n=0

for i in nota:
    if i<=7:
        n+=1
print(f'A quantidade de notas abaixo de 7 é: {n}')

print('Fim')