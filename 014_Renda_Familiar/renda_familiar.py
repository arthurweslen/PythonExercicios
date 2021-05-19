print('='*28)
print(f'\033[1:7m{"RENDA FAMILIAR":=^28}\033[m')
print('='*28)

renda = (input('Digite o valor de sua renda familiar (R$): '))
while not renda.isnumeric():
    renda = input('Digite o valor de sua renda familiar (R$): ')


if int(renda) > 0 and int(renda) <= 324:
    print('Conforme o Governo Federal - Você se encaixa no grupo: \033[1:31mExtremamente Pobre\033[m')

elif int(renda) > 324 and int(renda) <= 648:
    print('Conforme o Governo Federal - Você se encaixa no grupo: \033[1:31mPobre, mas não extremamente\033[m')

elif int(renda) > 648 and int(renda) <= 1164:
    print('Conforme o Governo Federal - Você se encaixa no grupo: \033[1:33mVulnerável\033[m')

elif int(renda) > 1164 and int(renda) <= 1764:
    print('Conforme o Governo Federal - Você se encaixa no grupo: \033[1:33mBaixa Classe Média\033[m')

elif int(renda) > 1764 and int(renda) <= 2564:
    print('Conforme o Governo Federal - Você se encaixa no grupo: \033[1:34m Média Classe Média\033[m')

elif int(renda) > 2564 and int(renda) <= 4076:
    print('Conforme o Governo Federal - Você se encaixa no grupo: \033[1:34m Alta Classe Méddia\033[m')

elif int(renda) > 4076 and int(renda) <= 9920:
    print('Conforme o Governo Federal - Você se encaixa no grupo: \033[1:32mBaixa Classe Alta\033[m')

elif int(renda) > 9920:
    print('Conforme o Governo Federal - Você se encaixa no grupo: \033[1:32mAlta Classe Alta\033[m')

