# teste = list()
# teste.append('Sabrina')
# teste.append(21)
#
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste)
# print(galera)

# lista = [['Sabrina', 21], ['João', 7], ['Janaina', 39], ['Raimundo', 44]]
# for p in lista:
#     print(f'{p[0]} tem {p[1]} anos', end=' = ')

galera = []
dado = []
totmaior = totmenor = 0
for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for v in galera:
    print(f'{v[0]} tem {v[1]} anos.')
    if v[1] >= 21:
        print(f'{v[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{v[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade.')
print(f'Temos {totmenor} menores de idade.')