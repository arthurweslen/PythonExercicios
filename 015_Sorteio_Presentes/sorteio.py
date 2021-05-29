print('='*28)
print(f'\033[1:7m{"SORTEIO DE PRESENTES":=^28}\033[m')
print('='*28)

#Importando a biblioteca Random, para escolher de forma randômica
import random
#Lista de nomes que será sortedo
nomes = ['Arthur','Laura','Tania','Sergio','Celia','Eduarda','Eduardo','Lenita','Weslen','Joyce']

print('Esses são os funcionários que estão concorrendo ao grande e misterioso presente!!!')
for x in nomes:
  print(x)

print('......Estamos sorteando!!')
input("Pressione ENTER para continuar")

#random.choice para escolher
sorteio = random.choice(nomes)
print('\033[1:34mParabéns {}\033[m, venha receber seu presente!'.format(sorteio))