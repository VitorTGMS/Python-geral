hora=input("Que horas você estuda, m para matutinu, v para vespertino e n para noturno")
hora=hora.upper()

if hora == 'M':
    print("Bom dia")
elif hora =='v':
    print("Boa tarde")
elif hora == 'N':
    print("Boa noite")
else:
    print("Valor invalido")