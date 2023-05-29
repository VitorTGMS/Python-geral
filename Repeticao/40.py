soma_vei=0
soma_aci=0
maior_aci=0
menor_aci=1000
for i in range(0, 5):
    cod=int(input(f'Digite o código da {i+1} cidade\n'))
    vei=int(input(f'Didite o número de veículos da {i+1} cidade\n'))
    aci=int(input(f'Digite o número de acidentes fatais da {i+1} cidade\n'))
    
    if aci>maior_aci:
        maior_aci=aci
        cod_maior_aci=cod
    
    if aci<menor_aci:
        menor_aci=aci
        cod_menor_aci=cod
        
    soma_vei+=vei
    soma_aci+=aci

print(f'A cidade com maior número de acidentes tem o codigo {cod_maior_aci} com {maior_aci} acidentes')
print(f'A cidade com menor número de acidentes tem o codigo {cod_menor_aci} com {menor_aci} acidentes')
print(f'A media de veiculos é de {soma_vei/5}')
print(f'A media de acidentes é de {soma_aci/5}')