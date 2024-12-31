sexo = str(input('Informe seu sexo: [F/M] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))