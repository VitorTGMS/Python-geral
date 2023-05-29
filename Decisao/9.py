n1=float(input("Digite o primeiro numero:"))
n2=float(input("Digite o segundo numero:"))
n3=float(input("Digite o terceiro numero:"))


maior=n1
menor=n1
medio=n1

if n1>=n2 and n1>=n3:
    maior=n1
    if n2>=n3:
        medio=n2
        menor=n3
    else:
        medio=n3
        menor=n2
elif n2>=n1 and n2>=n3:
    maior=n2
    if n1>=n3:
        medio=n1
        menor=n3
    else:
        medio=n3
        menor=n1
else:
    maior=n3
    if n1>=n2:
        medio=n1
        menor=n2
    else:
        medio=n2
        menor=n1

print(maior, medio,menor)
