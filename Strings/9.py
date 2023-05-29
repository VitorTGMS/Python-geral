cpf=input('Digite seu cpf')

pri,seg,ter = cpf.split('.')
terc, quar=ter.split('-')

if len(pri)>3 or len(seg)>3 or len(terc)>3 or len(quar)>2:
    print('cpf invalido')
    
try:
    pri=int(pri)
    terc=int(terc)
    seg=int(seg)
    quar=int(quar)
    print('Cpf valido')
except ValueError:
        print('Cpf invalido')
        