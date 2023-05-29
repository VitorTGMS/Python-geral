def quadrados_magicos():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    quadrados = []
    
    # Gera todas as permutações possíveis dos números
    permutacoes = __import__('itertools').permutations(numeros)
    
    for permutacao in permutacoes:
        a, b, c, d, e, f, g, h, i = permutacao
        
        # Verifica se a soma das linhas, colunas e diagonais é igual
        if a + b + c == d + e + f == g + h + i == a + d + g == b + e + h == c + f + i == a + e + i == c + e + g:
            quadrado_magico = [[a, b, c], [d, e, f], [g, h, i]]
            quadrados.append(quadrado_magico)
    
    # Imprime os quadrados mágicos encontrados
    for quadrado in quadrados:
        for linha in quadrado:
            print(' '.join(str(numero) for numero in linha))
        print()
        
# Chama a função para identificar e mostrar os quadrados mágicos
quadrados_magicos()