import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "algoritmo", "desenvolvimento"]
    palavra = random.choice(palavras)
    return palavra

def exibir_palavra(palavra, letras_corretas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao.strip()

def jogar_forca ():
    palavra = escolher_palavra()
    letras_corretas = set()
    tentativas = 6

    print("Jogo da Forca")
    print("A palavra tem", len(palavra), "letras")
    print(exibir_palavra(palavra, letras_corretas))

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            letras_corretas.add(letra)
            print("A palavra é:", exibir_palavra(palavra, letras_corretas))
        else:
            tentativas -= 1
            print("-> Você errou pela", 6 - tentativas, "ª vez. Tente de novo!")

        if tentativas == 0:
            print("Você foi enforcado! A palavra correta era:", palavra)
            break

        if set(palavra) == letras_corretas:
            print("Parabéns! Você acertou a palavra:", palavra)
            break

jogar_forca()