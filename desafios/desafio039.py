from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = - (ano - date.today().year)
if idade < 18:
    print('\033[1;31mVocê ainda tem que se alistar ao serviço militar. Mas não se preocupe, falta {} meses para se alistar!\033[m'.format(- (idade - 18) * 12))
elif idade == 18:
    print('\033[32mChegou o ano de se alistar ao serviços militares!\033[m')
else:
    print('\033[35mEspero que tenha se alistado, já passou {} meses do prazo de alistamento.\033[m'.format((idade - 18) * 12))
print('\033[33m{} anos nunca é tarde para começar.'.format(idade))
