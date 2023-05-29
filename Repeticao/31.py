n=float(input('Digite o valor da mercadoria'))
soma=0

while n!=0:
    soma+=n
    n=float(input('Digite o valor da próxima mercadoria, caso não haja, digite 0:'))

r=float(input(f'O valor total da compra foi {soma}, digite o valor pago pelo cliente'))
tro=r-soma

print(f'O valor do troco será: {tro}')