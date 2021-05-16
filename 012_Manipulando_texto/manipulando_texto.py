print('='*28)
print(f'\033[1:7m{"Maniplulando":=^28}\033[m')
print('='*28)

#Declarando a variavel frase
frase = 'Esse programa é feito totalmente em Python, esse sever apenas como aprendizagem, para MANIPULAR textos! - Python Exercices'

#Print da Frase com cor Azul, Negrito e Sublinhado
print('\n\033[1:4:34mFrase Original \033[m')
print('\033[1:34m'+frase+'\033[m')

#Upper() variável maiúscula
print('\n\033[1:4mTudo Maiúsculo\033[m')
print(frase.upper())

#lower deixa a variável minúscula
print('\n\033[1:4mTudo Minúsculo\033[m')
print(frase.lower())

#Replace troca as palavras do texto
print('\n\033[1:4mTrocar Palavras\033[m')
print(frase.replace('programa','Software'))
print(frase.replace('a','•',2))

print('\n\033[1:4mConta Letras, Sílavas ou Palavras\033[m')
print('• Quantas letras "a" minuscula tem: ',frase.count('a'))
print('• Quantas letras "a" tem no total: ',frase.lower().count('a'))
print('• Quantas sílavas "ar" tem no total: ',frase.lower().count('ar'))

print('\nExiste a palavra Python na frase? ','PYTHON' in frase.upper())
print('Existe a palavra Android na frase? ','Android' in frase.upper())

print('\nLocalização da palavra Python a partir do 0: ',frase.lower().find('python'))#localizou o primeiro python
print('Localização da palavra Python a partir do 25: ',frase.lower().find('python',25))#localizou o primeiro python
print('Localização da palavra Python a partir do 50: ',frase.lower().find('python',50))#Localizou o segundo python

#virar uma lista e imprimir
frase_divida = frase.split()
print('\n\033[1:4mPalavra 10º da lista:\033[m\n',frase_divida[10])
print('\n\033[1:4mPalavra 10º da lista letra 2:\033[m\n',frase_divida[10][2])
print('\033[1:4mPalavra 10º até o 12º da lista: \033[m\n',frase_divida[10:12])
print('\033[1:4mFrase Completa lista: \033[m\n',frase_divida)