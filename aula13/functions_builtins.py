import re
"""
sempre leia a documentação!
"""

# criado uma calculadora que realiza operações de somma com funções built-in

numero1 = input('Digite o primeiro número: ')
numero2 = input('Digite o segundo número: ')

# tratando exceções --> Forma falha de tratamento(não aceita números negativos)
"""
if numero1.isdecimal() and numero2.isdecimal():
    numero1 = float(numero1)
    numero2 = float(numero2)
    print(numero1+numero2)
else:
    print('Digite números válidos!!!')
"""

# Tratando exceções com com 'Try' e 'Exception' --> é mais eficiente
"""
try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    print(numero1+numero2)
except:
    print('ERROR!')
"""

# Extendendo funções built-in para criar funcionalidades eficientes:
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


###########
#  USAGE  #
###########

if is_number(numero1) and is_number(numero2):
    numero1 = float(numero1)
    numero2 = float(numero2)

    print(numero1 + numero2)
else:
    print('Error!')



