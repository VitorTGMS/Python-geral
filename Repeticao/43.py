cod={"100":0, "101":0, "102":0, "103":0, "104":0, "105":0}
t=0
while True:
    r=input("Deseja pedir alguma coisa? S ou N?")
    r=r.upper()
    if r!='S':
        break
    n=int(input("Código do pedido"))
    quant=int(input("Informe a quantidade"))
    if n==100:
        cod["100"]=quant*1.2
        t+=cod["100"]
    elif n==101:
        cod["101"]=quant*1.3
        t+=cod["101"]
    elif n==102:
        cod["102"]=quant*1.5
        t+=cod["102"]
    elif n==103:
        cod["103"]=quant*1.2
        t+=cod["103"]
    elif n==104:
        cod["104"]=quant*1.3
        t+=cod["104"]
    elif n==105:
        cod["105"]=quant*1
        t+=cod["105"]
    else:
        print('Codigo invalido')

print(f"O valor total de Cachorro quente foi: {cod['100']}")
print(f"O valor total de Bauru simples foi: {cod['101']}")
print(f"O valor total de Bauru com ovo foi: {cod['102']}")
print(f"O valor total de Hambúrguer foi: {cod['103']}")
print(f"O valor total de Cheeseburguer foi: {cod['104']}")
print(f"O valor total de Refrigerante foi: {cod['105']}")
print(f"O valor total do pedido foi: {t}")
