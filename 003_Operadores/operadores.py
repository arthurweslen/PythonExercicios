print('='*28)
print(f'\033[1:7m{"OPERADORES MATEMATICA":=^28}\033[m')
print('='*28)

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))

soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2
exponenciacao = num1**num2
modulo = num1 % num2
divisaoint = num1 // num2

print('{} + {} é igual a {}'.format(num1,num2,soma))
print('{} - {} é igual a {}'.format(num1,num2,subtracao))
print('{} / {} é igual a {}'.format(num1,num2,divisao))
print('{} * {} é igual a {}'.format(num1,num2,multiplicacao))
print('{} // {} é igual a {}'.format(num1,num2,divisaoint))
print('{} % {} é igual a {}'.format(num1,num2,subtracao))
print('{} ** {} é igual a {}'.format(num1,num2,exponenciacao))