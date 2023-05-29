par=0
im=0
for i in range(0, 10):
    n=float(input(f'Digite o numero {i+1}:'))
    if n%2==0:
        par+=1
    else:
        im+=1
print(f'A quantidade de numeros pares é {par} e a quantidade de numeors impares é {im}')