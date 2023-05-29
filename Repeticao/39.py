maior_altu=0
menor_altu=1000

for i in range(0, 3):
    cod=int(input(f'Digite o código do aluno {i+1}\n'))
    altu=float(input('Digite sua altura'))
    
    if altu>maior_altu:
        maior_altu=altu
        cod_maior_altu=cod
        
    if altu<menor_altu:
        menor_altu=altu
        cod_menor_altu=cod

print(f'A altura do maior aluno é {maior_altu}\nE seu código é {cod_maior_altu}')
print(f'A altura do menor aluno é {menor_altu}\nE seu código é {cod_menor_altu}')