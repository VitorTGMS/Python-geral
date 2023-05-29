cod=int(input('Digite seu código'))
maior_gor=0
menor_gor=1000
maior_altu=0
menor_altu=1000

cod_maior_gor=cod
cod_menor_gor=cod
cod_maior_altu=cod
cod_menor_altu=cod

while cod!=0:
    gor=float(input('Digite seu peso em kg'))
    altu=float(input('Digite sua altura em metros'))
    
    if gor>maior_gor:
        maior_gor=gor
        cod_maior_gor=cod
    
    if gor<menor_gor:
        menor_gor=gor
        cod_menor_gor=cod
        
    if altu>maior_altu:
        maior_altu=altu
        cod_maior_altu=cod
    
    if altu<menor_altu:
        menor_altu=altu
        cod_menor_altu=cod
    
    cod=int(input('Digite um novo código ou digite 0 para encerrar:'))

print(f'O mais gordo é {maior_gor}\nSeu codigo é {cod_maior_gor}')
print(f'O mais magro é {menor_gor}\nSeu codigo é {cod_menor_gor}')
print(f'O mais alto é {maior_altu}\nSeu codigo é {cod_maior_altu}')
print(f'O mais anão é {menor_altu}\nSeu codigo é {cod_menor_altu}')