def notas(* num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a sintuação da turma.
    """
    sm = 0
    tot = 0
    alunos = dict()
    for soma in num:
        sm += soma
        tot += 1
    alunos['total'] = tot         # ou poderia usar o sum(num) / len(num)
    alunos['maior'] = max(num)
    alunos['menor'] = min(num)
    alunos['média'] = sm / tot
    if sit:
        if alunos['média'] >= 7:
            alunos['situação'] = 'BOA'
        elif alunos['média'] >= 5:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'RUIM'
    return alunos


resp = notas(5.5, 5.5, 4.5, 10, 6.5, sit=True)
print(resp)
print(help(notas))