lista=['a','b','c','d','e','f','g','h','i', 'j']
conso=[]
a=0
for i, n in enumerate(lista):
    if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
        a
    else:
        conso.append(n)

for i, n in enumerate(conso):
    print(n)

print(len(conso))