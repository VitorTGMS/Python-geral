def mes_extenso(mes):
    meses = [
     'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
     'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
 ]
    return meses[mes-1]
def formatar_data(data):
    dia,mes,ano=data.split('/')
    
    if len(dia) !=2 or len(mes)!=2 or len(ano)!=4:
        return "NULL"
    
    try:
        dia=int(dia)
        mes=int(mes)
        ano=int(ano)
        
        if dia<1 or dia >31 or mes <1 or mes>12:
            return "NULL"
        elif mes==2:
            if ano%4==0 and dia>29:
                return "NULL"
            elif dia>28:
                return "NULL"
        elif mes%2==0 and dia>30:
            return "NULL"
        
        nome_mes=mes_extenso(mes)
        return f"{dia} de {nome_mes} de {ano}"
    except ValueError:
        return "NULL"

data=input("Digite uma data no formato DD/MM/AAAA")
data_extenso=formatar_data(data)

print(data_extenso)