print('='*28)
print(f'\033[1:7m{"NUMERO DIGITADO":=^28}\033[m')
print('='*28)

num = int(input('Digite um número: '))
print('Número digitado: {} \nNúmero antecessor: {} \nNúmero posterior: {}'. format(num,num-1,num+1))