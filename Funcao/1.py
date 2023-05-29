def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = ' '.join([str(i)]*i)
        print(linha)

# Solicita o valor de n ao usuário
n = int(input("Digite um valor inteiro: "))

# Chama a função para imprimir o padrão
imprimir_padrao(n)