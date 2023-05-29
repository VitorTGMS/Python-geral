arquivo=open('usuario.txt', 'r')

linha=arquivo.read()

lista=linha.split()


nome=lista[::2]
bite=lista[1::2]

print('ACME Inc.', ' '*10, 'Uso do espaço em disco pelos usuários')
print('-'*70)
print('Nr. Usuário', ' '*15, 'Espaço ulilizado', ' '*5, '% do uso')

bite_int=[int(num)/1000000 for num in bite]

i=0

for n in nome:
    percentual=bite_int[i]/sum(bite_int)*100
    print('{}  {:<10} {:>25.2f}MB {:>15.2f}%'.format(i+1, n, bite_int[i], percentual))
    i+=1
arquivo2=open('relatorio.txt', 'w')
i=0


arquivo2.write('ACME Inc.            Uso do espaço em disco pelos usuários\n')
arquivo2.write('----------------------------------------------------------------------\n')
arquivo2.write('Nr. Usuário                 Espaço ulilizado       % do uso\n')
for n in nome:
    percentual=bite_int[i]/sum(bite_int)*100
    arquivo2.write('{}  {:<10} {:>25.2f}MB {:>15.2f}%\n'.format(i+1, n, bite_int[i], percentual))
    i+=1
arquivo.close()
arquivo2.close()