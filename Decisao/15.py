l1=float(input("Digite o primeiro lado:"))
l2=float(input("Digite o Segundo lado:"))
l3=float(input("Digite o Terceiro lado:"))

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    if l1==l2==l3:
        print("É um triangulo equilatero")
    elif l1==l2 or l1==l3 or l2==l3:
        print("É um triangulo isóceles")
    else:
        print("É um triangulo escaleno")
else:
    print("não é um triangulo")