frase=input('Digite uma frase')
frase=frase.lower()

frase=frase.replace(' ','')
invert_frase=frase[::-1]

if frase==invert_frase:
    print('Palindromo')
else:
    print('Não é palindromo')
