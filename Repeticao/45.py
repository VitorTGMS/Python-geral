gab=["A","B","C","D","E","E","D","C","B","A"]
nomes=[]
soma=0
somat=0
notas=[]
alunos=0

while True:
    nome=input("Digite seu nome")
    nomes.append(nome)
    if nome=='':
        break
    for i in range (0, 10):
        r=input(f"Digite a resposta da {i+1}ª questão\n")
        r=r.upper()
        if r==gab[i]:
            soma+=1
    notas.append(soma)
    alunos+=1

max_nota=max(notas)
min_nota=min(notas)

print(f"O total de alunos que usaram o programa foi: {alunos}")
print(f"O maior número de acertos foi: {max_nota}")
print(f"O menor número de acertos foi: {min_nota}")
somat=sum(notas)
print(f"A média da turma foi:{somat/alunos}")