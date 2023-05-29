def nome_mes(mes):
    meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]
    return meses[mes - 1]


data=input('Digite sua data de nascimento no formato DD/MM/AAAA')

dia, mes, ano=data.split('/')
dia=int(dia)
mes=int(mes)
ano=int(ano)
if dia<1 or dia>31 or mes<1 or mes>12:
    print('Data invalida')
    
elif dia > 29 or (dia == 29 and not (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))):
    print('Data invalida')
elif mes%2==0 and dia>30:
    print('Data invalida')
else:
    print(f'{dia} de {nome_mes(mes)} de {ano}')