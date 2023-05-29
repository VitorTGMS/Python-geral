num=int(input('Montar a tabuada de:'))
com=int(input('Começar por:'))
ter=int(input('Terminar em:'))
while com>ter:
    print('Valor de começo maior que término, tente novamente')
    com=int(input('Começar por:'))
    ter=int(input('Terminar em:'))
print(f'Vou montar a tabuada do {num}, começando em {com} e terminando em {ter}')

for i in range(com, ter+1):
    print(f'{num} X {i} = {num*i}')