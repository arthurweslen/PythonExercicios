print('='*28)
print(f'\033[1:7m{"NÚMERO INTEIRO":=^28}\033[m')
print('='*28)

from math import floor
num = float(input('Digite um número decimal: '))
num_int = floor(num)

print('O número {} é um número decimal. Ele inteiro fica: \033[1:4m{}\033[m'.format(num,num_int))