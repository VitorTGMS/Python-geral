print("Responda as perguntas com S ou N")
soma=0

res=(input("Telefonou para a vitima?"))
res=res.upper()

if res=='S':
    soma=soma+1
res=(input("Esteve no local do crime?"))

res=res.upper()

if res=='S':
    soma=soma+1

res=(input("Mora perto da vitima?"))
res=res.upper()

if res=='S':
    soma=soma+1

res=(input("Devia paara a vitima?"))
res=res.upper()

if res=='S':
    soma=soma+1

res=(input("Já trabalhou com a vitima?"))
res=res.upper()

if res=='S':
    soma=soma+1

if soma==5:
    print("Assassino")
elif soma>=3:
    print("Cúmplice")
elif soma==2:
    print("Suspeita")
else:
    print("Inocente")
    