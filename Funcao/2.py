def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = ' '.join([str(j) for j in range(1, i+1)])
        print(linha)

# Solicita o valor de n ao usuário
n = int(input("Digite um valor inteiro: "))

# Chama a função para imprimir o padrão
imprimir_padrao(n)