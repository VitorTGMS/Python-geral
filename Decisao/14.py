n1=float(input("Digite a primeira parcial:"))
n2=float(input("Digite a segunda parcial:"))

m=(n1+n2)/2

if m>=9:
    print("Aprovado com A, sua media foi:",m)
elif m>=7.5 and m<9:
    print("Aprovado com B, sua media foi:",m)
elif m>=6 and m<7.5:
    print("Aprovado com C, sua media foi:",m)
elif m>=4 and m<6:
    print("Reprovado com D, sua media foi:",m)
else:
    print("Reprovado com E, sua media foi:",m)
