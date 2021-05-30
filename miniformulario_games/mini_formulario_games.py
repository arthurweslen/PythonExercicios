#Essas primeiras linhas são apenas um título, com cores invertidas
print('='*29)
print(f'\033[1:7m{"FORMULÁRIO RAPIDO PARA JOGOS":=^28}\033[m')
print('='*29)

resposta = 'N'
#jogadas = ('','Pedra','Papel','Tesoura')
#numPermitidos = [1,2,3]

opcoes = ('Feminino','Masculino')

while resposta == 'N':
    nome = input('Digite seu nickname ou nome: ')
    print('Seja vem vindo {}'.format(nome))

    sexo = input('Qual seu sexo [F/M]: ').upper()
    while sexo != 'M' and sexo != 'F':
        print('Olá {}, digite F para feminino e M para masculino'.format(sexo))
        sexo = input('Qual seu sexo [F/M]: ').upper()

    game = input('Você prefere nossa versão Mobile ou Console [M/C:] ').upper()
    while game != 'M' and game != 'C':
        game = input('Olá {}, digite "M" para Mobile ou "C" para Console [M/C]: '.format(nome)).upper()

    if sexo == 'M':
        sexo = 'Masculino'
    elif sexo == 'F':
        sexo = 'Feminino'
    if game == 'M':
        game = 'Mobile'
    elif game == 'C':
        game = 'Console'

    print('-='*20)
    print('Confirme seus dados: ')
    print('Seu nome: {}'.format(nome))
    print('Seu Sexo: {}'.format(sexo))
    print('Você prefere: {}'.format(game))

    resposta = input('Seus dados estão corretos? [S/N]').upper()
    print('-=' * 20+'\n')
print('FIM')
