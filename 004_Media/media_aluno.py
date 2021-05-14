#Essas primeiras linhas são apenas um título, com cores invertidas
print('=====================================')
print('\033[1:7m MÉDIA DAS NOTAS DOS ALUNOS\033[m')
print('===================================== \n')

nota1 = float(input('Digite a 1º nota do aluno: '))
nota2 = float(input('Digite a 2º nota do aluno: '))
media = (nota1 + nota2)/2

print ('A média do aluno é de {}'.format(media))