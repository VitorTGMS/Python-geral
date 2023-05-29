a=int(input('Digite um número'))
b=int(input('Digite um número'))
s=0
if a>b:
    for i in range(b, a):
        print(i)
        s=s+i
else:
    for i in range(a, b):
        print(i)
        s=s+i
print('A soma dos numeros comprendidos no intervalo é:',s)