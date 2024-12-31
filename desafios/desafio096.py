print('Controle de Terrenos')
print('-' * 20)

def area(largura, complimento):
    soma = largura * complimento
    print(f'A área de um terreno {largura}x{complimento} é de {soma:.1f}m².')


area(largura = float(input('LARGURA (m): ')), complimento = float(input('COMPLIMENTO (m): ')))
