perg={"Telefonou para a vítima?":0, "Esteve no local do crime?":0,"Mora perto da vítima?":0, "Devia para a vítima?":0,"Já trabalhou com a vítima?":0}
print('Responda com S ou N')
for i, n in enumerate(perg):
    res=input(n)
    res=res.upper()
    
    if res=='S':
        perg[n]+=1

if sum(perg.values())<2:
    print('Inocente')
elif sum(perg.values())==2:
    print('Suspeita')
elif sum(perg.values())>2 and sum(perg.values())<5:
    print('Cumplice')
else:
    print('Assassino')