lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# se eu precisar da numeração
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# se eu não precisar da posição do numero
for comida in lanche:
    print(f'Apartir de agora só vou comer {comida}')

# se eu precisar da númeração
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!!')
print(f'Eu tenho quantos nomes dentro dessa tuplas: {len(lanche)}')
