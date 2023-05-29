r=input('Deseja adicionar uma temperatura? S ou N?')
r=r.upper()
i=0
mai=-1000
men=1000
total=0
while r=='S':
    t=float(input('Digite o valor da temperatura'))
    if t>mai:
        mai=t
    if t< men:
        men=t
    total+=t
    i+=1
    r=input('Deseja adicionar uma nova temperatura? S ou N?')
    r=r.upper()

print(f'A maior temperatura será {mai}')
print(f'A menor temperatura será {men}')
m=total/i
print(f'A temperatura média será {m}')