n1 = float(input('Qual é o preço do produto? '))
r = (n1 * 5) / 100
t = n1 - r
print('Com 5% de desconto você receberá um desconto de R${:.2f} \nTotal do produto com desconto:R${:.2f}'.format(r, t))
