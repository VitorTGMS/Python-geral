string1=input('Digite uma string')
string2=input('Digite outra string')

print(f'{string1} tem {len(string1)}\n{string2} tem {len(string2)}')
    
if len(string1)==len(string2):
    if string1==string2:
        print('As duas strings são iguais')
    else:
        print('As duas strings tem o mesmo tamanho, porém são diferentes')
else:
    print('As duas strings tem tamanho diferente')
