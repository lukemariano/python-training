import datetime

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se
no horário descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

horas = input('Digite que horas são agora: ')
minutos = input('Digite os minutos relativos a hora digitada: ')

try:
    horas = int(horas)
    minutos = int(minutos)
    horario = datetime.time(hour=horas, minute=minutos)

    if 0 <= horas <= 11:
        print(f'Bom dia! O horário é: {horario}')
    elif 12 <= horas <=17:
        print(f'Boa tarde! O horário é: {horario}')
    else:
        print(f'Boa noite! O horário é: {horario}')
except:
    print('Digite uma hora ou minuto válido!')

