n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('-=-' * 25)
print('Com uma nota {:.1f} e {:.1f}, sua média foi de {:.1f}'.format(n1, n2, media))
if media < 5:
    print('Infelizmente \033[1;31m você está REPROVADO!\033[m')
elif media > 6.9:
    print('PARABÉNS, você está \033[1;32mAPROVADO!!\033[m')
elif media >=5: #if 7 > media >=5:
    print('Você ficou de \033[1;33mRECUPERAÇÃO\033[m')
print('Não desista dos estudos!!')
