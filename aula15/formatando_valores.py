"""
Formatando valores com modificadores - Aula 15

<variável>:s - Texto (strings - str)
<variável>:d - Inteiros (int)
<variável>:f - Números de ponto flutuante (float)
<variável>:.(NÚMERO-casas)f - Quantidade de casas decimais de um número tipo float
<variável>:(CARACTERE-PREENCHER)(> ou < ou ^)(quantidade de vezes repetir)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

SÓ FUNCIONA EM F STRINGS
ljust()
rjust() --> ambos podem ser úteis
"""

# exemplo de usos dos modificadores
num1 = 1
print(f'{1:.2f} {type(1)}')

print(f'{num1:<10}') # adiciona espaço em branco a direita da variável

print(f'{num1:0^11}')

print(f'{num1:0>4}')

# combinando modificadores
print(f'{num1:0>5.2f}')