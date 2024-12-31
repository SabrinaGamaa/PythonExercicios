n1 = input('Digite seu nome completo: ')
nome = n1.split()
primeiro = nome[0]
ultimo = nome[-1]
#.format(nome[len(nome)-1]))
print('Seu nome é: {}\nSeu primeiro nome é: {}\nSeu ultimo nome é: {}'.format(n1, primeiro, ultimo))
