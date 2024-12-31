frase = input('Digite uma frase: ').strip().upper().replace(' ', '').upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
inverso1 = junto[::-1]
'''for  letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]'''
print('Você digitou a seguinte frase:\n{}\nA frase ao contrario ficará:\n{}'.format(junto, inverso1))
if inverso1 == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palindromo.')


