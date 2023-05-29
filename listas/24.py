import random

resultado=[0,0,0,0,0,0]
for i in range(100):
    dado=random.randint(1,6)
    resultado[dado-1]+=1

for i in range(6):
    print(f'Numero {i+1} foi conseguido {resultado[i]} vezes')