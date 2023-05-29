numero=float(input("Digite um numero menor que 1000"))
n=numero
if numero>1000:
    print("Numero invalido")
    exit(0)
    
cem=n//100
if cem == 1:
    cemp="centena"
else:
    cemp="centenas"

n=n-cem*100

dez=n//10

if dez==1:
    dezp="dezena"
else:
    dezp="dezenas"

n=n-dez*10

if n==1:
    unip="unidade"
else:
    unip="unidades"

print(f'O numero {numero} tem {cem} {cemp}, {dez} {dezp} e {n} {unip}')