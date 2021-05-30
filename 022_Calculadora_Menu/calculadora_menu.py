print('='*28)
print(f'\033[1:7m{"CALCULADORA":=^28}\033[m')
print('='*28)

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

print(f'\n\033[1m{"MENU DE OPERAÇÕES":=^20}\033[m')

print('[1] - SOMA')
print('[2] - SUBTRAÇÃO')
print('[3] - DIVISÃO')
print('[4] - MULTIPLICAÇÃO')
print('[5] - EXPONENCIAÇÃO')
print('[6] - MÓDULO')
print('[7] - DIVISÃO INTEIRO')
print('[8] - NOVOS NÚMEROS')
print('[9] - SAIR')
print('=-'*10)
operacao = int(input('Escolha uma das opções do menu acima: '))

while operacao>=1 and operacao <=9:
    if operacao == 1:
        print('A soma de {} + {} é igual a : {}'.format(num1,num2,num1+num2))
        operacao = int(input('Escolha uma das opções do menu acima: '))
    elif operacao == 2:
        print('A subtração de {} - {} é igual a : {}'.format(num1,num2,num1-num2))
        operacao = int(input('Escolha uma das opções do menu acima: '))
    elif operacao == 3:
        print('A divisão de {} / {} é igual a : {}'.format(num1,num2,num1/num2))
        operacao = int(input('Escolha uma das opções do menu acima: '))
    elif operacao == 4:
        print('A multiplicação de {} * {} é igual a : {}'.format(num1,num2,num1*num2))
        operacao = int(input('Escolha uma das opções do menu acima: '))
    elif operacao == 5:
        print('A soma de {} ** {} é igual a : {}'.format(num1,num2,num1**num2))
        operacao = int(input('Escolha uma das opções do menu acima: '))
    elif operacao == 6:
        print('O Módulo de {} % {} é igual a : {}'.format(num1,num2,num1%num2))
        operacao = int(input('Escolha uma das opções do menu acima: '))
    elif operacao == 7:
        print('A divisão do número inteiro de {} // {} é igual a : {}'.format(num1, num2, num1//num2))
        operacao = int(input('Escolha uma das opções do menu acima: '))
    elif operacao == 8:
        print('Novos Números')
        num1 = int(input('Digite o 1º número: '))
        num2 = int(input('Digite o 2º número: '))
        operacao = int(input('Escolha uma das opções do menu acima: '))
    elif operacao == 9:
        import sys # IMPORTANDO A BIBLIOTECA, PARA ENCERRAR O PRORAMA AQUI
        sys.exit('O program será encerrado!!!') #COMANDO PARA ENCERRAR O PROGRAMA AQUI

import sys # IMPORTANDO A BIBLIOTECA, PARA ENCERRAR O PRORAMA AQUI
sys.exit('OPÇÃO INVÁLIDA, o programa esta sendo encerrado!!!') #COMANDO PARA ENCERRAR O PROGRAMA AQUI