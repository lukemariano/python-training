"""
A função 'len()' chama o método '__len__()' de uma variável, uma vez que tudo em python é um objeto,
as strings herdam métodos e propriedades de seu construtor String();
"""

# Vamos verificar se o usuário digitado possui no mínimo 6 caracteres antes de inseri-lo no nosso database
usuario = input('Digite o seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('O usuário precisa ter no mínimo 6 carcateres!')
else:
    print('Usuário cadastrado com sucesso!')

# Utilizando o método len no lugar da função
print(usuario.__len__())
