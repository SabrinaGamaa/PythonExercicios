def jogadores(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato')



nome = str(input('Nome do Jogador: '))
num = str(input('Número de Gols: '))
if num.isnumeric():
    num = int(num)
else:
    num = 0

if nome.strip() == '':
    jogadores(g=num)
else:
    jogadores(nome, num)


