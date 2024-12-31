num = input('Digite a expressão: ')
pilha = []
for simb in num:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está certa.')
else:
    print('Sua expressão está errada.')



