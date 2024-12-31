print('\033[1;34m-=-\033[m' * 30)
n1 = float(input('Qual é o valor do seu salário: R$ '))
print('\033[36m-=-\033[m' * 30)
dez = (n1 * 10) / 100
quinze = (n1 * 15) / 100
if n1 >= 1250:
    print('Seu salário com aumento de 10% ficará R${:.2f}'.format(n1 + dez))
else:
    print('Seu salário com aumento de 15% ficará R${:.2f}'.format(quinze + n1))
