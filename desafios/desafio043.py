peso = float(input('Qual é o seu peso em kg? '))
altura = float(input('Qual é sua altura? '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('Seu IMC está \033[35m{:.1f}, Isso quer dizer que você está abaixo do peso recomendado para sua saúde\033[m. Por favor, tome mais cuidado.'.format(imc))
elif imc < 25:
    print('Seu IMC está \033[34m{:.1f}, Isso quer dizer que seu peso está o ideal\033[m. Continue cuidando do seu corpo!'.format(imc))
elif imc < 30:
    print('Seu IMC está \033[33m{:.1f}, Isso quer dizer que seu peso está um pouco acima do recomendado para sua saúde\033[m. Por favor, tome mais cuidado.'.format(imc))
elif imc < 40:
    print('Seu IMC está \033[31m{:.1f}, Isso quer dizer que você acima do peso, já é considerado obesidade\033[m. Tenter cuidar melhor de sua saúde.'.format(imc))
else:
    print('Seu IMC está \033[31m{:.1f}, Você está em uma sintuação delicada, sua obesidade já é considerada mórbida\033[m. Por favor, procure um médico.'.format(imc))
print('Cuide do seu corpo e sua saúde mental, isso é fundamental para ter uma vida bem sucedida.')
