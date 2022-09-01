"""
Faça um programa que peça para o usuário digitar um número inteiro,
informe se esse número é par ou impar. Caso o usuário não digite um
número inteiro, informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)

    if numero % 2 == 0:
        print(f'{numero} é um número par.')
    else:
        print(f'{numero} é um número ímpar.')
except:
    print('Não é um número inteiro ou Não é um número válido!')

