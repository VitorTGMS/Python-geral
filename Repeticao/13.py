ba=int(input('Digite a base'))
e=int(input('Digite o expoente'))
b=ba
for i in range(1, e):
    b=b*ba
print(b)