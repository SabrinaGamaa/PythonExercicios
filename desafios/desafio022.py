nome = input('Digite seu nome Completo: ')

print('Nome maiúsculo:\n', nome.upper())
print('Nome minúsculas:\n', nome.lower())

xespaco = nome.replace(' ', '').strip() #len(nome) - nome.count(' '))
print('Quantas letras tem o nome:\n', len(xespaco))

p1 = nome.split()
print('Quantas letras tem o primeiro nome:\n', len(p1[0]))
