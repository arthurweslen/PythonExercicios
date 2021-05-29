#Essas primeiras linhas são apenas um título, com cores invertidas
print('='*28)
print(f'\033[1:7m{"EMPRESTIMO BANCÁRIO":=^28}\033[m')
print('='*28)

#Criação de variáveis, mas se o usuário digitar letra ou cactere especial, fica repetindo
imovel = input('Digite o Valor do Imóvel(R$): ')
while not imovel.isnumeric():
    imovel = input('Digite o Valor do Imóvel(R$): ')

salario = input('Digite o Valor do seu Salário(R$): ')
while not salario.isnumeric():
    salario = input('Digite o Valor do seu Salário(R$): ')

parcela = input('Será didivido em quantas parcelas : ')
while not parcela.isnumeric():
    parcela = input('Será didivido em quantas parcelas : ')

prestacao = float(imovel)/int(parcela)



#Se o valor da prestação for maior que 30% do salario, empréstimo bloeado
if prestacao > (0.3 * float(salario)):
    print('\n'+'=' * 80)
    print('\033[1:31m Empréstimo bloqueado,\033[m o valor da parcela é de: {}'.format(prestacao))
    print('Realizamos os cálculos do seu salário, só será realizado o emprestimo se a parcela for menor ou igual a \033[1:31m R${}\033[m '.format(0.3 * float(salario)))

#Se o valor da prestação for menor ou igual a 30% do salario, empréstimo aceito
else:
    print('\n'+'=' * 80)
    print('\033[1:32m PARABÉNS, O banco aprovou seu empréstimmo\033[m!!!')
    print('\033[1m Sua parcela ficou no valor de: R${} em {} vezes\033[m'.format(prestacao,parcela))

