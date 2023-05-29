n1=float(input("Digite a primeira parcial"))
n2=float(input("Digite a segunda parcial"))
n3=float(input("Digite a terceira parcial"))

m=(n1+n2+n3)/3

if m==10:
    print("Aprovado com distinção")
elif m>= 7:
    print("Aprovado")
else:
    print("Reprovado")