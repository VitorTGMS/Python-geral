saltos=[]

while True:
    nome=input("Nome do atleta: ")
    if nome=='':
        break
    
    for i in range(0, 5):
        distancia=float(input(f"{i+1}º Salto: "))
        saltos.append(distancia)
        
        max_salto= max(saltos)
        min_salto= min(saltos)
        media_saltos=(sum(saltos)-max_salto-min_salto)/3
        
    print(f"Atleta: {nome}")
        
    for i, saltos in enumerate(saltos):
        print(f"{i+1}º Salto: {saltos}m")
    print(f"Melhor salto: {max_salto}m")
    print(f"Pior salto: {min_salto}m")
    print(f"Média dos demais saltos: {media_saltos}")
    
    print(f"Resultado final:\n{nome}:{media_saltos}")
    
    saltos=[]