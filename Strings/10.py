uni={1:'um', 2:'dois',3:'tres',4:'quatro',5:'cinco',6:'seis',7:'sete',8:'oito',9:'nove',10:'dez',11:'onze', 12:'doze',13:'treze',14:'quatorze',15:'quinze',16:'dezeseis',17:'dezesete',18:'dezoito', 19:'dezenove'}
dez={20:'vinte', 30:'trinta', 40:'quarenta', 50:'cinquenta', 60:'sesenta', 70:'setenta',80:'oitenta', 90:'noventa'}
while True:
    n=int(input('Digite um número menor que 99: '))
    if n>99:
        break
    deze=n//10
    deze=deze*10


    if deze>=20:
        unid=n-deze
        print(f'{dez[deze]} e {uni[unid]}')
    else:
        print(uni[n])