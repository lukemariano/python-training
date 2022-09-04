"""
Elementos ou valores iteráveis são aqueles que possuem indíces que podem ser percorridos por um laço de repetição,
por exemplo.
"""

# iterando strings
frase = 'Eu sou lindo'
tamanho_frase = frase.__len__()
nova_frase = ''
contador = 0

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'u':
        nova_frase += letra
    else:
        nova_frase += letra.upper()
    contador += 1

print(nova_frase)
