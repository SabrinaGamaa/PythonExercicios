pessoas = dict()
lista = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas["nome"] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo != 'F' and sexo != 'M':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    pessoas["sexo"] = sexo
    pessoas["idade"] = int(input('Idade: '))
    soma += pessoas["idade"]
    lista.append(pessoas.copy())

    sair = str(input('Quer continuar? [N/S] ')).upper().strip()[0]
    while sair != 'S' and sair != 'N':
        print('ERRO! Por favor, digite apenas S ou N.')
        sair = str(input('Quer continuar? [N/S] ')).upper().strip()[0]
    if sair == 'N':
        break

print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A média de idade é {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ' , end='')
for p in lista:
    if p["sexo"] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista de pessoas que estão acima da média: ', end='')
for p in lista:
    if p["idade"] >= media:
        print('     ', end='')
        for k , v in p.items():
            print(f'{k} = {v}; ', end='')
    print()
print('--> ENCERRADO <--')
