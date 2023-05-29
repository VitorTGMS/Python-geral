notas=[]

while True:
    nome=input("Digite o nome do atleta")
    if nome=='':
        break
    for i in range (0, 7):
        nota=float(input(f"Digite a {i+1} nota"))
        notas.append(nota)
    max_nota=max(notas)
    min_nota=min(notas)
    media_notas=(sum(notas)-max_nota-min_nota)/5
    
    for i, notas in enumerate(notas):
        print(f"{i+1}ª nota: {notas}")
    print("Resultado final")
    print(f"Alteta: {nome}")
    print(f"Melhor nota:{max_nota}")
    print(f"Pior nota:{min_nota}")
    print(f"Média:{media_notas}")