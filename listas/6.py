medias=[]
m=0
for i in range(0,10):
    print(f'Digite as notas do aluno {i+1}')
    for j in range(0,4):
        n=int(input(f'digite a {i+1} nota'))
        m+=n
    m=m/4
    if m>=7:
        medias.append(m)
    m=0

print(f'O número de alunos com a nota maior que 7 é {len(medias)}')