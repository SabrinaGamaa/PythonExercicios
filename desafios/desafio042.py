n1 = float(input('Digite a primeira medida: '))
n2 = float(input('Digite a segunda medida: '))
n3 = float(input('Digite a terceira medida: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('As médidas acima PODEM formar um triângulo ', end='')
    if n1 == n2 and n2 == n3:
        print('\033[31mEQUILÁTERO!\033[m (todos os lados iguais.)')
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print('\033[32mISÓSCELES!\033[m (dois lados iguais).')
    elif n1 != n2 != n3:
        print('\033[33mESCALENO!\033[m (todos os lados diferentes.)')
else:
    print('As medidas acima NÃO PODEM formar um triângulo!')
