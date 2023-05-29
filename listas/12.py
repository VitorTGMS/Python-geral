idade=[]
altura=[]
m=0
n=0
for i in range(0,30):
    ida=int(input(f'Digite a idade da aluna {i+1}'))
    alt=float(input(f'Digite a altura da aluna {i+1}'))
    idade.append(ida)
    altura.append(alt)
        
m=sum(altura)/30
for i in range(0,30):
    if idade[i]>=13 and altura[i]>=m:
        n+=1

print(f'O número de alunos com idade de 13 anos e altura maior que a média é {n}')