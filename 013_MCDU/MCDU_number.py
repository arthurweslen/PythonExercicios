print('='*28)
print(f'\033[1:7m{"MCDU":=^28}\033[m')
print('='*28)

num = input('Digite um número de número qualquer: ')
mcdu = str(num)

while not num.isnumeric() or int(num) >=10000 or int(num) < 0:
    num = input('Digite um número de número de 0 a 9999: ')
    mcdu = str(num)

print('='*28)
if int(num) < 10 and int(num) >=0:
    print('Unidade é : {} '.format(mcdu[0]))
elif int(num) >= 10 and int(num) < 100:
    print('Unidade é : {} '.format(mcdu[1]))
    print('Dezena é : {} '.format(mcdu[0]))
elif int(num) >= 100 and int(num) < 1000:
    print('Unidade é : {} '.format(mcdu[2]))
    print('Dezena é : {} '.format(mcdu[1]))
    print('Centena é : {} '.format(mcdu[0]))
elif int(num) >= 1000 and int(num) < 10000:
    print('Unidade é : {} '.format(mcdu[3]))
    print('Dezena é : {} '.format(mcdu[2]))
    print('Centena é : {} '.format(mcdu[1]))
    print('Milhar é : {} '.format(mcdu[0]))




