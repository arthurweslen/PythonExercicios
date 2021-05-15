print('='*28)
print(f'\033[1:7m{"IMPORT":=^28}\033[m')
print('='*28)

#importando biblioteca matemática e randomico
import math
import random

texto = input('Aperte ENTER para o computador gerar um número aleatório')
num = random.randint(0,9999999)
raiz = math.sqrt(num)
arrendodar_cima = math.ceil(raiz)
arrendodar_baixo = math.floor(raiz)

print('Número gerado randômicamente: \033[1:7m{}\033[m'.format(num))
print('\n\033[1:4mRaiz quadrada:\033[m {}'.format(raiz))
print('\033[1:4mArredondar a Raiz para baixo:\033[m  {} \n\033[1:4mArredondar Raiz para Cima:\033[m  {}'.format(arrendodar_baixo,arrendodar_cima))

