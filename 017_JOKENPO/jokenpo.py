#Essas primeiras linhas são apenas um título, com cores invertidas
print('='*28)
print(f'\033[1:7m{"VAMOS JOGAR JOKENPO":=^28}\033[m')
print('='*28)

import random
jogadas = ('','Pedra','Papel','Tesoura')
numPermitidos = [1,2,3]
jkp_pc = random.choice(numPermitidos)

print('Digite 1 para PEDRA \nDigite 2 para PAPEL \nDigite 3 para TESOURA')
print('='*28)

jkp = int(input('Qual opção você deseja escolher: '))

while jkp > 3 or jkp < 1:
    jkp = int(input('Qual opção você deseja escolher: (1, 2 ou 3)'))

#Importando para fazer o programa escrever JO KEN PO de um em um segundo
from time import sleep
print('= '*7)
print('JO')
sleep(1)
print('   KEN')
sleep(1)
print('      PO!!!')
sleep(1)
print('= '*7)

print('\033[1mVocê escolheu: {}\033[m'.format(jogadas[jkp]))
print('\033[1mO computador escolheu: {}\033[m'.format(jogadas[jkp_pc]))

if jkp == jkp_pc:
    print('\033[1:33mUALLL - DEU EMPATE!!!\033[m')
elif jkp == 1 and jkp_pc ==3:
    print('\033[1:34mPedra ganha de Tesoura, então você GANHOU\033[m')
elif jkp == 1 and jkp_pc ==2:
    print('\033[1:31mPedra perde para Papel, então você PERDEU\033[m')
elif jkp == 2 and jkp_pc ==1:
    print('\033[1:34mPapel ganha da Pedra, então você GANHOU\033[m')
elif jkp == 2 and jkp_pc ==3:
    print('\033[1:31mPapel perde para Tesoura, então você PERDEU\033[m')
elif jkp == 3 and jkp_pc ==1:
    print('\033[1:31mTesoura perde para Pedra, então você PERDEU\033[m')
elif jkp == 3 and jkp_pc ==2:
    print('\033[1:34mTesoura ganha do Papel, então você Ganhou\033[m')