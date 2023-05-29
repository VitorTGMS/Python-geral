n=int(input('Digite quantos numeros tem no conjunto'))
mai=None
men=None
soma=0
for i in range(0, n):
    num=int(input((f'Digite o {i+1} numero')))
    if num>mai:
        mai=num
    if num<men:
        men=num
    soma=soma+num

print('O menor numero é:', men)
print('O maior numero é:', mai)
print('A soma dos numeros é:',soma)