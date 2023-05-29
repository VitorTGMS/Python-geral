dia=float(input("Digite o dia"))
mês=float(input("Digite o mês"))
ano=float(input("Digite o ano"))

if dia>31 or mês>12 or dia<0 or mês<0:
    print("Data invalida")
elif mês==2 and ano%4!=0 and dia>28:
    print("Data invalida")
elif mês==2 and ano%4==0 and dia>29:
    print("Data invalida")
elif mês%2!=0 and dia==31:
    print("Data invalida")
else:
    print("Data valida")
    