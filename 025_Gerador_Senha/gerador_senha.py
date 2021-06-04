#Titulo para o programa
print('='*28)
print(f'\033[1:7m{"GERADOR DE SENHA":=^28}\033[m')
print('='*28)

#Importando as bibliotecas RANDOM, STRING e TIME
import random, string, time

#Variável com input de 3 linhas
escolha = input('''\033[1:31mS\033[m para senha \033[1:31mSimples\033[m
\033[1:33mC\033[m para senha \033[1:33mComum\033[m
\033[1:34mF\033[m para senha \033[1:34mForte\033[m          
O que você deseja: [S/C/F]:''').upper()

#IF se for igual a S - simples
if escolha == 'S':
    tamanho = 4
    chars = string.digits
    rnd = random.SystemRandom()
    print('\033[1:31mSenha fraca são apenas 4 caracteres numérico\033[m')
    print('Estamos criando.... ')
    time.sleep(2)
    #join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é: '+''.join(rnd.choice(chars) for i in range(tamanho))+'\033[m')
elif escolha == 'C':
    tamanho = 8
    chars = string.ascii_lowercase + string.digits
    rnd = random.SystemRandom()
    print('\033[1:33mSenha comum são 8 caracteres (letras minúsculas e números)\033[m ')
    print('Estamos criando.... ')
    time.sleep(2)
    #join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é: '+''.join(rnd.choice(chars) for i in range(tamanho))+'\033[m')
elif escolha == 'F':
    tamanho = 16
    chars = string.ascii_letters + string.digits + '!@#$%¨&*()_-+=´`^~[{]},.?ç\///'
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha é forte, contendo números, letras minúsculas, maiúsculas, e caracteres especiais\033[m')
    print('Estamos criando.... ')
    time.sleep(2)
    #join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é: '+''.join(rnd.choice(chars) for i in range(tamanho))+'\033[m')
else:
    # Se digitar qualquer outra coisa sem ser F,C,S - encerra o programa
    print('Estamos com dificuldade para processar, aguarde....... ')
    time.sleep(2)
    print("Opção não identificada \n")
    time.sleep(1)
    import sys
    sys.exit('Programa está sendo encerrado, tente mais tarde!')

