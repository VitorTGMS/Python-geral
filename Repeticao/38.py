sal=1000
psal=0.015

for i in range(1996, 1998):
    sal=sal+sal*psal
    psal=psal*2
print(sal)

salf=float(input('Digite o salário do funcionário'))
psalf=0.015

for i in range(1996, 1998):
    salf=salf+salf*psalf
    psalf=psalf*2
salf=round(salf,2)
print(salf)