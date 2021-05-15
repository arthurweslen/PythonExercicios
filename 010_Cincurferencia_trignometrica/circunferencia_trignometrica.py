print('='*28)
print(f'\033[1:7m{"CIRCUNFERÊNCIA TRIGONOMÉTRICA":=^28}\033[m')
print('='*28)

from math import cos, tan, sin
angulo = int(input('Digite o valor do angulo: '))
cosseno = cos(angulo)
tangente = tan(angulo)
seno = sin(angulo)

print('O Valor de seno é \033[1:34m{}\033[m'.format(seno))
print(' O Valor de cosseno é \033[1:32m{}\033[m'.format(cosseno))
print('O Valor da tangente é \033[1:35m{}\033[m'.format(tangente))