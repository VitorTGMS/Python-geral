carros=[]
consumo=[]

for i in range(5):
    print(f'Veículo {i+1}')
    car=input('Nome:')
    carros.append(car)
    con=float(input('Km por litro:'))
    consumo.append(con)
    
print('Relatório Final')
for i in range(5):
    km=1000/consumo[i]
    custo=km*2.25
    print("{}-{:<10}-{:>5}-{:>8.2f} litros - R${:>5.2f}".format(i+1, carros[i],consumo[i], km, custo))