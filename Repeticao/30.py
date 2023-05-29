n=int(input('Digite a quantidade de pães:'))
v=0
while n>50:
    n=int(input('Quantidade de pães excedentes tente novamente:'))
for i in range(0, n):
        v=v+0.18
v=round(v,2)
print(f'O valor total a pagar será {v}')