"""
Entendendo debbug e utilizando laço de repetição 'WHILE'
Enquanto determinada condição for verdadeira, execute o bloco de códigos em seu escopo
"""

# x = 0

# Passo 1: colocar o breakpoint no início do loop e depois clicar no inseto
# while x < 10:
#     print(x)
#     x += 1

"""
Sempre que a palavra reservada 'continue' estiver presente em um loop, as instruções posteriores a ela
não serão mais executadas, porque o continue simplesmente irá retornar para o início do loop
"""
# z = 0
#
# while z < 6:
#     if z == 3:
#         z += 1
#         continue
#     print(z)
#     z += 1
#
# print('Acabou!')

"""
A palavra reservada 'break' --> finaliza o LOOP
"""

# Gerando coordenadas ou linhas e colunas com aninhamento de WHILES loop

x = 0

while x < 10:
    y = 0
    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1

"""
O que acontece no bloco de intruções acima é que ao entrar no PRIMEIRO while loop,
o y é setado com o valor 0, em seguida entra no bloco de códigos que verifica se y é menor do que 5.
E para cada valor de x de 0 a 9 será executado um while loop para Y, tendo valores variando de 0 a 4.
"""
