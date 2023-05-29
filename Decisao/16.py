a=float(input("Digite 'a' da equação do segundo grau"))
if a==0:
    print("Não é uma equação do segundo grau")
    exit()

b=float(input("Digite 'b' da equação do segundo grau"))
c=float(input("Digite 'c' da equação do segundo grau"))

delt=(b*b)-(4*a*c)

if delt<0:
    print("As raízes da equação não pertencem ao conjunto de numeros reais")
    exit()
elif delt==0:
    eq=(-b)/(2*a)
    print("A equação possui apenas uma raíz e ela é:", eq)
else:
    eq=(-b+delt)/(2*a)
    eq2=(-b-delt)/(2*a)
    print(f'A equação possui duas raizes:{eq} e {eq2}')
    