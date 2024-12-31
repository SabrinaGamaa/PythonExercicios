dados = dict()
lista = list()
gols = 0
cont = 0
dados['nome'] = str(input('Nome do Jogador: '))
qpartidas = int(input(f'Quantas Partidas {dados["nome"]} jogou? '))
for g in range(0, qpartidas):
    lista.append(int(input(f'Quantos gols na {g + 1}º partida? ')))
    gols = sum(lista)
dados['gols'] = lista[:]
lista.clear()
dados['total'] = gols
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, e in dados.items():
    print(f'O campo {k} tem o valor {e}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {qpartidas} partidas.')
for i, v in enumerate(dados["gols"]):
    print(f'    => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {gols} gols.')
