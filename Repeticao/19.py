n=int(input('Digite quantos numeros tem no conjunto'))
print('Observação: os números devem estar entre 0 e 1000')
mai=0
men=1000
soma=0
i=0
for i in range(0, n):
    num=int(input((f'Digite o {i+1} numero')))
    while num > 1000 or num < 0:
        print('Número invalido')
        num=int(input(f'Digite o {i+1} numero'))
        
    if num>mai:
        mai=num
    if num<men:
        men=num
    soma=soma+num

print('O menor numero é:', men)
print('O maior numero é:', mai)
print('A soma dos numeros é:',soma)