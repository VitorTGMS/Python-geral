salarios = [0] * 9

while True:
    vendas_brutas = float(input("Digite o valor das vendas brutas (ou -1 para encerrar): "))
    if vendas_brutas == -1:
        break
    salario = 200 + (0.09 * vendas_brutas)
    if salario >= 1000:
        salarios[8] += 1
    else:
        indice = int((salario - 200) // 100)
        salarios[indice] += 1

intervalos = ["$200 - $299", "$300 - $399", "$400 - $499", "$500 - $599",
              "$600 - $699", "$700 - $799", "$800 - $899", "$900 - $999", "$1000 em diante"]

print("Quantidade de vendedores em cada intervalo de salários:")
for i in range(len(intervalos)):
    print(intervalos[i] + ":", salarios[i])
