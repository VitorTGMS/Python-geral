respostas={"Windows Server":0,"Unix":0,"Linux":0,"Netware":0,"Mac OS":0,"Outro":0}
total=0

print('Qual o melhor sistema operacional para uso em servidores?')
print('1-Windows Server\n2-Unix\n3-Linux\n4-Netware\n5-Mac OS\n6-Outro')

while True:
    voto=int(input('Digite o seu voto'))
    if voto==0:
        break
    while voto<1 or voto>6:
        voto=int(input('Voto inválido'))
    if voto == 1:
        respostas["Windows Server"] += 1
    elif voto == 2:
        respostas["Unix"] += 1
    elif voto == 3:
        respostas["Linux"] += 1
    elif voto == 4:
        respostas["Netware"] += 1
    elif voto == 5:
        respostas["Mac OS"] += 1
    elif voto == 6:
        respostas["Outro"] += 1
    total += 1


print("Resultado da votação:")
print("Sistema Operacional   Votos   %")
print("-------------------   -----   ---")

for sistema, votos in respostas.items():
    percentual=(votos/total)*100
    print("{:<20s} {:>6d} {:>5.1f}%".format(sistema, votos, percentual))
print("-------------------   -----   -----")
print("{:<20s} {:>6d}".format("Total", total))