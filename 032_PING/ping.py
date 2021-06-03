# -*- coding: cp1252 -*-
# coding=<encoding name>
#Essas primeiras linhas são apenas um título, com cores invertidas
print('='*28)
print(f'\033[1:7m{"PING ":=^28}\033[m')
print('='*28)

#importando biblioteca OS (integra os recursos do sistema operacional)
import os
# coding=<encoding name>
ip_host = input('Digite o IP ou Host para ser verificado: ')
qtd = input('Quantos pacotes deseja a ser verificado: ')

while not qtd.isnumeric():
    sair = input('Deseja \033[1:31mCancelar\033[m a verificação [S/N]: ').upper()
    if sair == 'S':
        import sys  # IMPORTANDO A BIBLIOTECA, PARA ENCERRAR O PRORAMA AQUI
        sys.exit('O programa será encerrado, verificação cancelada!!!')  # COMANDO PARA ENCERRAR O PROGRAMA AQUI
    elif sair == 'N':
        x=1
        while not qtd.isnumeric() and x<=3:
            print('-=' * 20)
            qtd = input('\033[1:34mQuantos pacotes deseja a ser verificado: \033[m')
            x +=1


os.system('ping -n {} {}'.format(qtd, ip_host)) #comando PING
print('-=' * 20)
