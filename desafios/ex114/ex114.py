import urllib.request

try:
    site = urllib.request.urlopen('https://www.whatsapp.com')
except Exception as erro:
    print(f'ERRO: {erro.__class__}')
else:
    print('Consegui acessar o site WhatsApp com sucesso!!')
    # html = site.read()
    # print(f'HTML de WhatsApp:\n{html}')

