#Essas primeiras linhas são apenas um título, com cores invertidas
print('='*28)
print(f'\033[1:7m{"CONTAGEM REGRESSIVA":=^28}\033[m')
print('='*28)

from time import sleep
for c in range (10,0,-1):
    #Essa linha serve para colocar os números no meio, entre 28 espaços
    print(f'{"{}": ^28}'.format(c))
    sleep(1)
sleep(1)
print('\033[1:34m     FELIZ ANO NOVO!!!   \033[m')

