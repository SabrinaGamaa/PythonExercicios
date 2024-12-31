pessoa = {'nome': 'Sabrina', 'sexo': 'F', 'idade': 21}
print(f'A {pessoa["nome"]} tem {pessoa["idade"]} anos.')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print('-=' * 35)

for k in pessoa.keys():
    print(k)

print('-=' * 35)
for v in pessoa.values():
    print(v)

print('-=' * 35)
for k, v in pessoa.items():
    print(k, v)

print('-=' * 35)
pessoa['peso'] = 55.5
print(pessoa)

print('-=' * 35)
pessoa['nome'] = 'Janaina'
print(pessoa)

print('-=' * 35)
del pessoa['sexo']
print(pessoa)
