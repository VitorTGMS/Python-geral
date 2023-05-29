saltos=[]

while True:
    nome=input("Nome do atleta: ")
    if nome=='':
        break
    
    for i in range(0, 5):
        distancia=float(input(f"{i+1}º Salto: "))
        saltos.append(distancia)
        

        media_saltos=sum(saltos)/5
        
    print(f"Atleta: {nome}")
        
    for i, saltos in enumerate(saltos):
        print(f"{i+1}º Salto: {saltos}m")

    print(f"Média dos saltos: {media_saltos}")
    
    print(f"Resultado final:\n{nome}:{media_saltos}")
    
    saltos=[]