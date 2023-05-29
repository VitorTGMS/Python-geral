saque=float(input("Digite o valor do saque"))
s=saque
nciq=0
ncic=0
ndez=0
nuni=0

if saque <10 or saque>600:
    exit(0)

ncem=saque//100

saque=saque-ncem*100
dez=saque//10

if dez>5:
    ndez=dez-5
    nciq=1
saque=saque-dez*10

if saque>5:
    ncic=1
    nuni=saque-5

print(f'Para sacar {s}, o programa fornece {ncem} notas de cem, {nciq} notas de ciquenta, {ndez} notas de dez, {ncic} notas de cinco e {nuni} notas de um')