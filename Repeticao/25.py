n=int(input('Digite o numero de pessoas'))
soma=0
m=0
for i in range(0, n):
    num=int(input(f'Digite a idade da {i+1} pessoa'))
    soma=soma+num

m=soma/n

if m>0 and m<=25:
    print('A turma é jovem')
elif m>=26 and m<=60:
    print('A turma é adulta')
else:
    print('A turma é idosa')
