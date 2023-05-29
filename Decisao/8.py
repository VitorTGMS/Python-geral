n1=float(input("Digite o primeiro produto:"))
n2=float(input("Digite o segundo produto:"))
n3=float(input("Digite o terceiro produto:"))

menor=n1

if n2<menor:
    menor=n2
if n3<menor:
    menor=n3

print("O menor preço é:", menor)