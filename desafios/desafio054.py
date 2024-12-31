from datetime import date
today = date.today().year
totmaior = 0
totmenor = 0
for nasceu in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(nasceu)))
    idade = today - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
print('E tivemos {} menores de idade.'.format(totmenor))
