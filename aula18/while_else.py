"""
While / Else
contadores (?) -> Garante a finalização de um laço WHILE / incrementa de forma linear
acumuladores (?) -> incrementa de forma não linear / é a soma do acumulador + contador
"""

# exemplo de acumulador
acumulador = 1
contador = 1

while contador <= 10:
    print(contador, acumulador)
    acumulador += contador
    contador += 1
else:
    print('Acabou o loop')

"""
A palavra resrvada 'break' anula a execução de um bloco 'else' de um loop.
O else só será executado quando a condição do loop for falsa;
"""
