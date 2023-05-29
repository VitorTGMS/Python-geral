n=int(input('Digite o numero de classes'))
m=0
soma=0
for i in range(0, n):
    alu=int(input((f'Digite a quantidade de alunos da turma {i+1}')))
    while alu>40:
        print('Quantidade de alunos invalidos')
        alu=int(input((f'Digite a quantidade de alunos da turma {i+1}')))
    soma=soma+alu
m=soma/n

print('A media de alunos por classe é:', m)