n=int(input('Digite um número inteiro diferente de 0'))
primo=[]
div=0
j=1
for i in range(1,n):
    Npri=None
    for j in range(2,i):
        if i%j==0:
            Npri=True
            div+=1
            break
        else:
            div+=1
    if Npri!=True:
        primo.append(i)
print(f'O número de números primos até {n} é {len(primo)}\n')
for i in primo:

    print(i, end=' ')
print(f'\nO numero de divisões feitas foi {div}')