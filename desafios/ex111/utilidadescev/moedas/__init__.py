def aumentar(preco=0, taxa=0, formato=False):
    """
    -> Calcule o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param preco: o preço que se quer reajustar
    :param taxa: qual é a taxa do aumento.
    :param formato: quer a sainda formatada ou não?
    :return: o valor reajustado, com ou sem formatação.
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moedas(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moedas(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moedas(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moedas(res)


def moedas(preco = 0, moedas = 'R$'):
    return f'{moedas}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=5, taxad=10):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR"}'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moedas(preco):}')
    print(f'Dodro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxad}% de redução: \t{diminuir(preco, taxad, True)}')
    print('-' * 30)
