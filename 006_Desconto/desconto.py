print('='*28)
print(f'\033[1:7m{"DESCONTO CELULARES":=^28}\033[m')
print('='*28)

celular = float(input('Digite o valor do celular: '))
print('O Celular nos dias úteis, terá o desconto de de 5% para quem pagar à vista. Valor reajustado:  {}'.format(celular*0.95))
print('O Celular nos feriados nacionais terá o desconto de 10%. Valor reajustado:  {}'.format(celular*0.90))
print('O Celular na black friday terá o desconto de 20%. Valor reajustado:  {}'.format(celular*0.80))
