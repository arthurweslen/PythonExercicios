#Essas primeiras linhas são apenas um título, com cores invertidas
print('='*28)
print(f'\033[1:7m{"PING ":=^28}\033[m')
print('='*28)

#importando biblioteca OS (integra os recursos do sistema operacional)
import os
import time

with open('./doc/host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('-='*25)
        print('Verificando o IP/Host do: \033[1:34m {}\033[m'.format(ip))
        print('....')
        time.sleep(3)
        os.system('ping -n 3 {}'.format(ip))
        print('-=' * 25)
        time.sleep(1)

