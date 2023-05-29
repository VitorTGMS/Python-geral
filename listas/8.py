idade=[]
alt=[]
n=0

for i in range (0,2):
    ida=int(input('Digite a sua idade'))
    idade.append(ida)
    
    altu=float(input('Digite a sua altura'))
    alt.append(altu)
    n+=1

for j in range(1, n+1):
    print(idade[-j])
    print(alt[-j])