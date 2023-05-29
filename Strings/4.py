nome=input('Digite seu nome')

caract=list(nome)

for i, nome in enumerate(nome):
        print(' '.join(caract[j] for j in range (0, i+1)))
