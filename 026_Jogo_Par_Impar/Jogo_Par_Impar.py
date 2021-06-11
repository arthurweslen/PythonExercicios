#Essas primeiras linhas são apenas um título, com cores invertidas
print('='*28)
print(f'\033[1:7m{"VAMOS JOGAR PAR OU IMPAR":=^28}\033[m')
print('='*28)

import random
import sys
vitorias = 0
tolerancia = 0


while True:
    print('=-'*20)
    num_pc = random.randrange(0, 11)  # randrange posso escolher quais os números que vai ser gerado randômicamente
    numero = input('Digite um número: ') # Digite um número
    if not numero.isnumeric(): #se o usuário digitar letra, o jogo encerra
        sys.exit('Desculpe, estamos encerrando, pois só aceitamos números')
    numero = int(numero) #converte o variavel número, para interiro
    resultado = num_pc + numero

    par = input('Par ou Ímpar: [P/I]').upper()
    while par != 'P' and par !='I' and tolerancia <=2:
        print('Digite P para Par e I para Impar')
        par = input('Par ou Ímpar: [P/I]').upper()
        tolerancia +=1

    if tolerancia >2:
        sys.exit('Você ultrapassou a quantidade de erros. O jogo está sendo encerrado')

    if resultado % 2 == 0 and par == 'P':
        print(f'O Computador escolheu {num_pc} e você escolheu {numero}')
        print('Parabéns, deu Par')
        vitorias += 1

    elif resultado % 2 != 0 and par == 'I':
        print(f'O Computador escolheu {num_pc} e você escolheu {numero}')
        print('Parabéns, deu Ímpar')
        vitorias += 1

    else:
        break

print('=-'*20)
print(f'O Computador escolheu {num_pc} e você escolheu {numero}')
print(f' \nVocê teve {vitorias} vitórias consecutivas')
print('GAME OVER')


