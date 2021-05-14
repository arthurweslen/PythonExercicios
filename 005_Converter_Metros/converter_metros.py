print('='*28)
print(f'\033[1:7m{"CONVERSÃO DE METROS":=^28}\033[m')
print('='*28)

metros = float(input('Digite um valor em metros: '))
kilometros = metros * 0.001
decametro = metros * 0.1
decimetros = metros * 10
centimetros = metros * 100
milimetros = metros * 1000

print ('{} metro(s) tem {} quilometo(s)'.format(metros,kilometros))
print ('{} metro(s) tem {} decametro(s)'.format(metros,decametro))
print ('{} metro(s) tem {} decimetros(s)'.format(metros,decimetros))
print ('{} metro(s) tem {} centimetros(s)'.format(metros,centimetros))
print ('{} metro(s) tem {} milimetro(s)'.format(metros,milimetros))