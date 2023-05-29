defeito={"Necessita de esfera":0, "Necessita de limpeza":0, "Necessita troca do cabo ou conector":0, "Quebrado ou inutilizado":0}
i=t=0
print('Situação')

for i, n in enumerate(defeito, 1):
    print('{}- {:<20}'.format(i+1, n))
    
while True:
    ident=float(input('Digite a identificação'))
    if ident==0:
        break
    sit = int(input('Digite o tipo de defeito: '))
    if 1 <= sit <= len(defeito):
        defeito[list(defeito)[sit-1]]+=1
        t+=1
print('situação', ' '*30,'Quantidade',' '*10,'Percentual')
i=0
for prob,quant in defeito.items():
    percentual=quant/t*100
    i+=1
    print('{}-{:<40} {:>5} {:>20}%'.format(i, prob, quant, percentual))
    