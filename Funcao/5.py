def somaImposto(taxaImposto,custo):
    custo=custo+custo*(taxaImposto/100)
    return custo

custo=float(input('Digite o custo do produto'))
taxaImposto=float(input('Digite a porcentagem de imposto sobre o produto'))

somaImposto(taxaImposto, custo)

print(somaImposto(taxaImposto, custo))