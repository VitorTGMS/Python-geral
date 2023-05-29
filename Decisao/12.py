hora=int(input('Digite a quantidade de horas'))
vhora=int(input('Digite o valor da hora'))

sal=vhora*hora

if sal<=900:
    ir=0
    r=0
elif 900<sal<=1500:
    ir=sal*5/100
    r=5
elif 1500<sal<=2500:
    ir=sal*10/100
    r=10
else:
    ir=sal*20/100
    r=20
inss=10*sal/100
fg=11*sal/100
sal_liq=sal-inss-ir

print('Salário Bruto:{}*{} : R${:>10.2f}'.format(vhora, hora, sal))
print('(-) IR ({}%)         : R${:>10.2f}'.format(r, ir))
print('(-) INSS (10%)      : R${:>10.2f}'.format(inss))
print('    FGTS (11%)      : R${:>10.2f}'.format(fg))
print('Total de descontos  : R${:>10.2f}'.format(ir+inss))
print('Salário Líquido     : R${:>10.2f}'.format(sal_liq))