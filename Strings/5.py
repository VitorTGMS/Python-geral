nome=input('Digite seu nome')

caract=list(nome)
n=len(nome)
for i in range(n, 0,-1):
    print(' '.join(caract[j] for j in range(0, i)))