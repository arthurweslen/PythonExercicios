#Essas primeiras linhas são apenas um título, com cores invertidas
print('='*28)
print(f'\033[1:7m{"VAMOS JOGAR ADIVINHAÇÃO":=^28}\033[m')
print('='*28)
#importando a biblioteca randomica
import random
num_pc = random.randrange(0,11) #randrange posso escolher quais os números que vai ser gerado randômicamente

print('Eu pensei em um número de 0 a 10, quero ver se você adivinhar')
num_user = input('Escolha um número de 0 a 10:  ')
tolerancia = 0 #variavel para usasr no WHILE

# SE O USUÁRIO DIGITAR UM CARACTER QUE NÃO SEJA NÚMERO, FAÇA ELE DIGITAR NOVAMENTE
while not num_user.isnumeric():
    num_user = input('Você não entendeu? Escolha um número de 0 a 10:  ')
    tolerancia += 1
    if tolerancia >=1:
        import sys # IMPORTANDO A BIBLIOTECA, PARA ENCERRAR O PRORAMA AQUI
        sys.exit('VOCÊ ESTÁ FAZENDO ISSO ERRADO! TENTE MAIS TARDE') #COMANDO PARA ENCERRAR O PROGRAMA AQUI

chance = 1 #variavel para verificar quantas vezes o usuário tentou até acertar
while int(num_user) != int(num_pc) and chance <3:
    print('Você errou, continue tentando')
    num_user = input('Escolha um número de 0 a 10:  ')
    chance += 1

print('-='*20)
#IF se acertar de primeira uns parabens, se for mais de 3 chances, perdeu e se for de segunda ou 3... acertou, mas não de primeira
if chance == 1:
    print('O número que eu pensei foi: {}'.format(num_pc))
    print('\033[1:32mPARABÉNS, VOCÊ ACERTOU DE PRIMEIRA\033[m') #texto  verde
elif chance >= 3:
    print('\033[1:31mVocê só tinha 3 chances, voce PERDEU.\033[m') #Texto vermelho
    print('O número que eu pensei foi: {}'.format(num_pc))
else:
    print('O número que eu pensei foi: {}'.format(num_pc))
    print('\033[1:33mAcertou, mas precisou de {} vezes para acertar\033[m'.format(chance)) #texto amarelo

