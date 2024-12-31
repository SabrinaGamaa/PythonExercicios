import moedas

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moedas.moedas(p)} é {moedas.moedas(moedas.metade(p))}')
print(f'O dobro de {moedas.moedas(p)} é {moedas.moedas(moedas.dobro(p))}')
print(f'Aumentando 10%, temos {moedas.moedas(moedas.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moedas.moedas(moedas.diminuir(p, 13))}')
