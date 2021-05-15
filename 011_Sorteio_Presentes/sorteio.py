print('='*28)
print(f'\033[1:7m{"SORTEIO DE PRESENTES":=^28}\033[m')
print('='*28)

#Importando a biblioteca Random, para escolher de forma randômica
import random
#Lista de nomes que será sortedo
nomes = ['Arthur','Laura','Tiago','Tania','Sergio','Celia','Eduarda','Eduardo','João','Pedro','Maria','Lenita','Weslen']
#random.choice para escolher
sorteio = random.choice(nomes)

print('Parabéns \033[1:34m{}\033[m, venha receber seu presente!'.format(sorteio))