print('='*28)
print(f'\033[1:7m{"PAR OU ÍMPAR":=^28}\033[m')
print('='*28)

num = int(input('\nDigite um número qualquer: '))
par = num % 2
if par == 0:
    print('\033[1:34mEsse número é par\033[m')
else:
    print('\033[1:31mEste número é impar\033[m')
