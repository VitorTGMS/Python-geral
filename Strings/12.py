num=input('Valida numero de telefone\nTelefone:')
nnum=num
nnum=nnum.replace('-', '')
if len(nnum)==7:
    novo_num='3'+num
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente')
    print(f'Telefone corrigido com formatação: {novo_num}')
    novo_num=novo_num.replace('-', '')
    print(f'Telefone corrigido sem formatação: {novo_num}')
else:
    novo_num=num
    print(f'Telefone corrigido com formatação: {novo_num}')
    novo_num=novo_num.replace('-', '')
    print(f'Telefone corrigido sem formatação: {novo_num}')
    