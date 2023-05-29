esp=0
a=0
e=0
i=0
o=0
u=0

frase=input('Digite uma frase')
frase=frase.lower()
esp=frase.count(' ')
a=frase.count('a')
e=frase.count('e')
i=frase.count('i')
o=frase.count('o')
u=frase.count('u')
print(f'Espaço apareceu {esp} vezes')
print(f'"A" apareceu {a} vezes')
print(f'"E" apareceu {e} vezes')
print(f'"I" apareceu {i} vezes')
print(f'"O" apareceu {o} vezes')
print(f'"U" apareceu {u} vezes')
