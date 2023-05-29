salario=float(input("Digite o seu salario"))

if salario <= 280:
    p=salario*0.2
    por=20
    salario2=salario + p
    
elif salario>280 and salario<=700:
    p=salario*0.15
    por=15
    salario2=salario + p
    
elif salario>700 and salario<=1500:
    p=salario*0.1
    por=10
    salario2=salario + p
else:
    p=salario*0.5
    por=5
    salario2=salario + p
    
print("O novo salario é:", salario2)
print("A porcentagem aplicada é de:", por, '%')
print("O valor aumentado foi de:", p)

