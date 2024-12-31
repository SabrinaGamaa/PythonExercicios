lista = []
alunos = dict()
alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input(f'Média de {alunos["nome"]}: '))
print('-=' * 30)
print(f'Nome é igual a {alunos["nome"].capitalize()}')
print(f'Média é igual a {alunos["media"]}')
if alunos["media"] >= 7:
    alunos["situação"] = 'APROVADO!'
elif 5 <= alunos["media"] < 7:
    alunos["situação"] = 'RECUPERAÇÃO'
else:
    alunos["situação"] = 'REPROVADO.'
lista.append(alunos.copy())
print(f'A situação de {lista[0]["nome"]} é igual a {lista[0]["situação"]}!')
print(lista)
