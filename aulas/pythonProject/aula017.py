lanche = ['Hambuerguer', 'Suco', 'Pizza', 'Pudim']
# Adiciona biscoito no ultimo
lanche.append('Biscoito')

#Adiciona o cachorro quente no 0
lanche.insert(0, 'Cachorro quente')
print(lanche)

#como remover
del lanche[3]
lanche.pop(3)
lanche.remove('pizza')
#se eu nao sei se tem pizza e desejo remover pizza
if 'pizza' in lanche:
    lanche.remove('pizza')

# se eu quiser os valores em ordem
valores = list(range(4, 11))
valores = [7, 4, 2, 6, 4, 8]
valores.sort()
# se eu quiser na ordem reversa
valores.sort(reverse=True)
# se eu quiser saber os valores que tem
len(valores)



num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 2)

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4 na lista')
print(num)
#colocar em ordem
#num.sort()

# elimina o escolhido na ordem
#num.pop(2)


print(f'Está lista tem {len(num)} elementos.')

