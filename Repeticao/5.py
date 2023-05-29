a=float(input('Digite a população A'))
ta=float(input('Digite a taxa de crecimento em A'))
ta=ta/100
b=float(input('Digite a população B'))
tb=float(input('Digite a taxa de crescimento em B'))
tb=tb/100
anos=0

while a<b:
    a=a+a*ta
    b=b+b*tb
    anos=anos+1
    
print('Para a população A se igualar ou ultrapassar a população B será necessário',anos,'anos')