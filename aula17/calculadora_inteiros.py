"""
Criando uma calculadora básica com aninhamento de laços de repetição WHILE
"""

while True:
    print()  # para pular uma linha após uma nova execução do LOOP
    n1 = input('Digite o primeiro número: ')
    n2 = input('Digite o segundo número: ')

    if not n1.isnumeric() or not n2.isnumeric():
        print('Digite um número válido!')
        continue

    operador = input('Digite um operador: +, -, / ou * ')

    if not n1.isnumeric() or not n2.isnumeric():
        print('Digite um número válido!')
        continue

    n1 = int(n1)
    n2 = int(n2)

    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '/':
        print(n1 / n2)
    elif operador == '*':
        print(n1 * n2)
    else:
        print('Operador inválido!')
        continue

    sair = input('Deseja sair? [s] ou [n]?')

    if sair == 's':
        break


