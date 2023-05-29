cd=int(input('Digite a quantidade de CDs:'))
soma=0
for i in range(0, cd):
    v=float(input(f'Digite o valor do {i+1} CD:'))
    soma=soma+v

m=soma/cd

print(f'O valor total da coleção de CD é {soma}, e a medía de valor é {m}')