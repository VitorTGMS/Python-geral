def retangulo (lin, col):
    if  col>20:
        print('O comprimento excedeu o limite, ele foi alterado para 20')
        col=20
    if lin>20:
        print('A largura excedeu o limite, ele foi alterado para 20')
        lin=20
    
    print('+', '-'*(col-2),'+')
    
    for i in range(1, lin+1):
        print('|', ' '*(col-2),'|')
    
    print('+', '-'*(col-2),'+')

col=int(input('Digite o comprimento do retangulo: '))
lin=int(input('Digite a altura do retangulo: '))

retangulo(lin, col)
