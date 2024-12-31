num = ''
while num != 'F' and 'M':
    print('-=' * 20)
    sexo = str(input('''Escolha seu estilo
[ F ] para feminino
[ M ] para masculino
Digite aqui: ''')).upper()
    if sexo != 'M' and sexo != 'F':
        print('\033[1;31mValor incorreto. Digite corretamente o valor.\033[m')
print('FIMmmmmmmmmmmm')

