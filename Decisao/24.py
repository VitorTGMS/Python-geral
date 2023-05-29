num=float(input("Digite um numero"))

print("Digite A para saber se ele é par ou impar")
print("Digite B para saber se ele é positivo ou negativo")
print("Digite C para saber se ele é inteiro ou decimal")

esc=(input("Escolha uma opção"))

esc = esc.upper()

if esc=='A':
    if num%2==0:
        print("O numero é par")
    else:
            print("O numero é impar")
elif esc == 'B':
    if num>0:
        print("O numero é positivo")
    else:
        print("O numero é negativo")
elif esc == 'C':
    if num == round(num):
        print("O numero é inteiro")
    else:
        print("O numero é decimal")
else:
    print("Alternativa invalida")