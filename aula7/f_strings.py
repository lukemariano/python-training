# f_strings

# calcule o seu IMC

nome = 'Lucas'
idade = 20
peso = 65
altura = 1.84
imc = peso / altura ** 2

print(f'{nome} tem {idade} de idade, e o seu IMC é: {imc:.2f}')

# utilizando format strings function

print('{} tem {} de idade, e o seu IMC é: {:.2f}'.format(nome, idade, imc))
# Dessa segunda forma, utilizamos a função format para substituir 'chaves' dentro da nossa STRING;
# onde os argumentos da função substituirão os espaços em branco em uma chave respectivamente;.
"""
Detalhe, dentro das chaves, pode-se passar o indice referente a um argumento da function format();
Isso só funcionará se for utilizado o indice do argumento em todas as chaves;
Também é possível utilizar argumentos nomeados como indice nas chaves;
"""
print('{1} {0} tem {2} de idade, e o seu IMC é: {0}'.format(nome, idade, imc))
