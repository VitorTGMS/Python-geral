nome=input('Digite um nome')

while len(nome)<3:
    print('Nome invalido, precisa haver mais que 3 caracteres')
    nome=input('Digite um nome')

idade=int(input('Digite sua idade'))

while idade<0 or idade>150:
    print('Idade invalida')
    idade=int(input('Digite sua idade'))

salario=float(input('Digite seu salário'))

while salario<0:
    print('Salário inválido')
    salario=float(input('Digite seu salário'))

sexo=input('Digite seu sexo (F ou M)')
sexo=sexo.upper()

while sexo!='F' and sexo!='M':
    print('Sexo invalido')
    sexo=input('Digite seu sexo (F ou M)')
    sexo=sexo.upper()

print('Digite seu estado civil')
print('S para solteiro')
print('C para casado')
print('V para viuvo')
print('D para Divorciado')

civ=input()
civ=civ.upper()

while civ !='S' and civ !='C' and civ !='V' and civ !='D':
    print('Estado civil inválido')
    civ=input()
    civ=civ.upper()
    
