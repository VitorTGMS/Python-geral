vet1=[1,3,5,7,9,11,13,15,17,19]
vet2=[2,4,6,8,10,12,14,16,18,20]
vet3=[30,40,50,60,70,80,90,100,110,120]
vet=[]
v1=0
v2=0
v3=0
for i in range(0,10):
    v1=vet1[i]
    v2=vet2[i]
    v3=vet3[i]
    vet.append(v1)
    vet.append(v2)
    vet.append(v3)

for i, n in enumerate(vet):
    print(n, end=',')