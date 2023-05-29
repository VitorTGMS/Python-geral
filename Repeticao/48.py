n=int(input("digite um número inteiro e positivo: "))

if n<0:
    print("Número inválido")
else:
    n_invertido=int(str(n)[::-1])
    print(f"Numero invertido: {n_invertido}")