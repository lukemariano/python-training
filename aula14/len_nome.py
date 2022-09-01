"""
Faça um programa que peça o primeiro nome do usuário.
Se o nome tiver 4 letras ou menos escreva "Seu nome é muito curto";
se tiver entre 5 e 6 letras escreva "Seu nome é normal";
maior que 6 letras escreva "Seu nome é muito grande".
"""
nome = input('Digite o seu primeiro nome: ')

tamanho_nome = nome.__len__()

if tamanho_nome == 0 or nome.isdigit():
    print('Nome inválido!')
else:
    if tamanho_nome <= 4:
        print('Seu nome é muito curto!')
    elif 5 <= tamanho_nome <= 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')


