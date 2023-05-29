n=int(input('Digite a quantidade de produtos:'))
v=0
while n>50:
    n=int(input('Quantidade de produtos excedentes tente novamente:'))
for i in range(0, n):
    v=v+1.99
v=round(v,2)
print(f'O valor total a pagar será {v}')