from datetime import date
print('Ano bissexto')
ano = int(input('digite o ano em que você está: ou digite 0 para analisar o seu ano atual'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))