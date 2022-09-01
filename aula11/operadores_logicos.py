"""
O operador lógico 'not' verifica se o condicional é 'false' --> se for, ele executo os blocos
de código em seu escopo;


"""

# Verificando se um determinado caracter está contido em uma palavra

"""
nome = "Lucas Mariano"

if 'z' in nome.lower():
    print("Existe")
else:
    print("Não existe.")

"""

# Validação de login básica:
usuario = input('Digite o usuario: ')
senha = input('Digite sua senha: ')

usuario_db = 'lancelor'
senha_db = 'gamerF0r3ver'

if usuario == usuario_db and senha == senha_db:
    print(f'O usuário {usuario_db} logou com sucesso!!!')
else:
    print('Usuário ou senha inválidos! Tente novamente.')


