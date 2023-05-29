a=80000
ta=0.03
b=200000
tb=0.015
anos=0

while a<b:
    a=a+a*ta
    b=b+b*tb
    anos=anos+1
    
print('Para a população A se igualar ou ultrapassar a população B será necessário',anos,'anos')