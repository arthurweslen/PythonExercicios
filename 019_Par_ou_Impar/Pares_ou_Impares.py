#Essas primeiras linhas são apenas um título, com cores invertidas
print('='*29)
print(f'\033[1:7m{"PARES/ÍMPARES DE 0 A 20":=^28}\033[m')
print('='*29)

print('Digite 1 para ver apenas os números ímpares de 0 a 20')
print('Digite 2 para ver apenas os números pares de 0 a 20 ')
print('Digite 3 para ver todos os números de 0 a 20')

num = int(input('O que você deseja? '))

if num == 1:
    print('\033[1mNÚMEROS ÍMPARES\033[m')
    for x in range(1,20,2):
        print(x)
elif num == 2:
    print('\033[1mNÚMEROS PARES\033[m')
    for x in range(0,21,2):
        print(x)
elif num == 3:
    print('\033[1mTODOS OS NÚMEROS\033[m')
    for x in range (0,21):
        print(x)
else:
    print('\033[1:31mOpção inválida\033[m')