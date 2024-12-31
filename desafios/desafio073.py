times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Intenacional', 'Fortaleza', 'São paulo',
         'Corinthias', 'Bahia', 'Cruzeiro', 'Vasco')

print(f'Lista de times: {times}')
print('-=' * 40)
print(f'Os 5 primeiros do Brasileirão é: {times[0:5]}')
print('-=' * 40)
print(f'Os 4 Ultimos colocados são:{times[-4:]}')
print('-=' * 40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 40)
print(f'O São Paulo está em {times.index("São Paulo")+1}º colocado')
print('-=' * 40)
