def horas (n,m):
    if n==0:
        horas_12=12
        periodo='A.M'
    elif n<12:
        horas_12=n
        periodo='A.M'
    elif n==12:
        horas_12=12
        periodo='P.M'
    else:
        horas_12=n-12
        periodo='P.M'
    return horas_12, m, periodo

def imprime_horas(horas, m, periodo):
    print(f'{horas}:{m:02d} {periodo}')

while True:
    n=int(input('Digite a hora'))
    m=int(input('Digite os minutos'))
    
    horas_12, m, periodo = horas(n, m)
    imprime_horas(horas_12, m, periodo)
    
    r=input('Deseja converter novo horário? S ou N?')
    r=r.upper()
    
    if r!='S':
        break