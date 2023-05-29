n=int(input("Digite um número inteiro positivo diferente de 0"))
print("S= 1/1", end='+')
m=1
soma=0
for i in range(1, n):
    m+=2
    soma=soma+(i+1/m)
    if i!=n-1:
        print(f"{i+1}/{m}", end='+')
    else:
        print(f"{i+1}/{m}")
soma=round(soma,2)
print(f"A soma total é:{soma}")