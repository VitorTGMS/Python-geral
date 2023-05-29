num=[]

for i in range(0,10):
    n=int(input('Digite um número'))
    num.append(n)

for i, n in enumerate(num):
    m=pow(n, 2)
    print(m)
