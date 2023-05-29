com=input("Digite o combustível, A para Alcool e G para gasolina")
L=float(input("Digite o numero de litros vendidos"))

com=com.upper()

if com == 'A':
    if 20>=L:
        pre=L*1.90
        des=pre*L*3/100
        pre=pre-des
    else:
        pre=L*1.90
        des=pre*L*5/100
        pre=pre-des
elif com =='G':
    if 20>=L:
        pre=L*2.5
        des=pre*L*4/100
        pre=pre-des
    else:
        pre=L*2.5
        des=pre*L*6/100
        pre=pre-des
else:
    exit()

print(f'O valor a ser pago pelo cliente é {pre}')