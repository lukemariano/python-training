"""

Operadores Relacionais (comparação)

== (igualdade) --> bool
>= (maior igual) --> bool
<= (menor igual) --> bool
< (menor) --> bool
> (maior) --> bool
!= (diferente) --> bool

Variáveis podem conter expressões

"""

# Exercicio para verificar se a pessoa tem idade para solicitar um empréstimo:

nome = input('Qual é o seu nome? \n')
idade = int(input('Qual é a sua idade? \n'))

valida_solicitacao = idade >= 18

if valida_solicitacao:
    print(f'O empréstimo pode ser concedido para {nome}')
else:
    print(f'{nome} não pode receber o empréstimo.')

ternario = 'De maior' if (idade > 20) else 'De menor'

print(ternario)




