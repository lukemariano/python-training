"""
Nome: str, idade: int, peso: float, altura: float, ano atual: int ---> data_nasc: int --> imc
"""

nome = 'Lucas'
idade = 20
peso = float(65)
altura = 1.84
ano_atual = 2022

# calculando IMC e ano atual
imc = peso / (altura ** 2)
data_nasc = ano_atual - idade


print(f'{nome} tem {idade} de idade, seu IMC é: {imc:.2f} e sua data de nascimento é: {data_nasc}')
