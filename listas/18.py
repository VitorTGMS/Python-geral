jogador={1:0, 2:0, 3:0, 4:0, 5:0, 6:0,7:0, 8:0, 9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0}
total=0

jogador_max=None
max_voto=0
print('Digite 0 para terminar')
while True:
    voto=int(input('Digite seu voto'))
    if voto==0:
        break
    while voto<1 or voto>23:
        voto=int(input('Voto inválido'))

    jogador[voto]+=1
    total+=1

for i in jogador:
    if jogador[i]>0:
        print(f'O jogador camisa {i} teve {jogador[i]} votos com {(jogador[i]/total*100):.2f}% dos votos')
    if jogador[i]>max_voto:
        jogador_max=i
        max_voto= jogador[i]

print(f'O jogador mais votado foi o {jogador_max} com {max_voto} votos e {(max_voto/total*100):.2f}% dos votos')
