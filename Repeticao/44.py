can={"Vitor":0, "Pablo":0, "Ruan":0, "Raíla":0, "nulo":0,"branco":0}
t=0
while True:
    vot=int(input("Digite seu voto\n1 para Vitor\n2 para Pablo\n3 para Ruan\n4 para Raíla\n5 para anular\n6 para votar em branco\n"))
    if vot==0:
        break
    elif vot==1:
        can["Vitor"]+=1
        t+=1
    elif vot==2:
        can["Pablo"]+=1
        t+=1
    elif vot==3:
        can["Ruan"]+=1
        t+=1
    elif vot==4:
        can["Raíla"]+=1
        t+=1
    elif vot==5:
        can["nulo"]+=1
        t+=1
    elif vot==6:
        can["branco"]+=1
        t+=1
    else:
        print("Voto invalido")

for i in can:
    print(f"O candidato {i} teve: {can[i]}")

print(t)
print(f"A porcentagem de votos nulos foi {can['nulo']/t*100}%")
print(f"A porcentagem de votos brancos foi {can['branco']/t*100}%")