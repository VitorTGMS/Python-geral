mes={"Janeiro":0, "Fevereiro":0, "Março":0, "Abril":0,"Maio":0,"Junho":0,"Julho":0, 
     "Agosto":0, "Setembro":0, "Outubro":0,"Novembro":0, "Dezembro":0}
m=0
for i, n in (mes):
    temp=float(input(f'Digite a temperatura de {n}'))
    mes[n]=temp
    m=m+temp

m=m/12

for n in mes:
    if mes[n]>=m:
        print(f'O mês de {n} teve temperatura acima da média')