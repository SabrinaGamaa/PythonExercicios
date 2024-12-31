numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte' )
while True:
    n1 = int(input('Digite um número de 0-20 para ter ele por extenso: '))
    if -1 < n1 <= 20:
        print(f'Seu número é {n1} e por extenso é: {numeros[n1]}')
        print('=' * 45)
        print('\033[31mPara sair digite -1\033[m ')
    if n1 == -1:
        break
print('-=-' * 20)
print('Obrigado pela preferência. Volte sempre!')
