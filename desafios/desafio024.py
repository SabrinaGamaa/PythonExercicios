nome = input('Digite seu nome: ').strip()
n1 = nome.lower().split()
# nome[:5] == 'Santos'
print('Este nome começa com santos?\n', 'santos' in n1[0])
