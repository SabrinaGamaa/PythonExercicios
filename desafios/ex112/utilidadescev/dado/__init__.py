def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha():
            print(f'ERRO! \033[0;31m\"{entrada}\"\033[m é um Preço inválido')
        else:
            valido = True
            return float(entrada)
