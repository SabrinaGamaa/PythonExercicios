from random import choice
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')
lista = [a1, a2, a3, a4]
sorteio = choice(lista)
print('A lista de alunos é: \n{}\n{}\n{}\n{}'.format(a1, a2, a3, a4))
print('=' * 30)
print('O aluno sorteado é: \n{}!!!!!!'.format(sorteio))

