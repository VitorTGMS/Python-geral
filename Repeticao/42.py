intervalos = {"[0-25]":0,"[26-50]":0, "[51-75]":0,"[76-100]":0}

while True:
    n=float(input('Digite um número'))
    if n<0:
        break
    elif n<=25:
        intervalos["[0-25]"]+=1
    elif n<=50:
        intervalos["[26-50]"]+=1
    elif n<=75:
        intervalos["[51-75]"]+=1
    else:
        intervalos["[76-100]"]+=1

print(f"Números no intervalo [0-25]: {intervalos['[0-25]']}")
print(f"Números no intervalo [0-25]: {intervalos['[26-50]']}")
print(f"Números no intervalo [0-25]: {intervalos['[51-75]']}")
print(f"Números no intervalo [0-25]: {intervalos['[76-100]']}")
        