a=int(input('Digite um número'))
b=int(input('Digite um número'))

if a>b:
    for i in range(b, a):
        print(i)
else:
    for i in range(a, b):
        print(i)