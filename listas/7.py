lista=[]
m=1

for i in range(0,5):
    n=int(input('Digite um número'))
    lista.append(n)

print(f'A soma de todos os números é: {sum(lista)}')

for i, j in enumerate(lista):
    m=m*j

print(f'A multiplicação de todos os números é: {m}')

