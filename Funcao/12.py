import random

def embaralha (nome):
    nome=nome.lower()
    caracteres=list(nome)
    random.shuffle(caracteres)
    
    nome_emba=''.join(caracteres)
    return nome_emba

nome=input("Digite uma palavra: ")

nomeEmb=embaralha(nome)

print(nomeEmb)