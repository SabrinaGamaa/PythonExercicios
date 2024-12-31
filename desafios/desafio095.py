jogador = dict()
gp = list()
time = list()
while True:
    gp.clear()
    jogador.clear()
    jogador["nome"] = str(input('Nome do Jogador: '))
    qpartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, qpartidas):
        gp.append(int(input(f'  Quantos gols na {p + 1}° partida: ')))
    jogador["gols"] = gp[:]
    total = sum(gp)
    jogador["total"] = total
    time.append(jogador.copy())
    while True:
        continua = str(input('Quer continuar? [N/S] ')).upper().strip()[0]
        if continua in 'SN':
            break
        print('\033[31mERRO! Por favor digite S ou N.\033[m')
    if continua == 'N':
        break
print(time)
print('-=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('--' * 30)
for k, c in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in c.values():
        print(f'{str(d):<15}', end='')
    print()
print('--' * 30)

while True:
    mostrar = int(input('Mostrar dados de qual Jogador? (999 para parar) '))
    if mostrar in range(0, len(time)):
        print(f'-- LEVANTAMENTO DO JOGADOR {time[mostrar]["nome"]}:')
        for n, j in enumerate(time[mostrar]['gols']):
            print(f'    No jogo {n + 1} fez {j} gols')
    if mostrar >= len(time):
        print(f'\033[31mERRO! Não existe jogador com codigo {mostrar}.\033[m')
    if mostrar == 999:
        break
print('--' * 5, f'{" VOLTE SEMPLE! ":^30}', '--' * 5)
