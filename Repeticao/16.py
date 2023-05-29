n=int(input('Digite o termo desejado:'))
soma=1
pro=1
ant=0

for i in range(1, n):
    soma=pro+ant
    ant=pro
    pro=soma
    if soma>500:
        break

print(soma)