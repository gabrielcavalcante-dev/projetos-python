# abra o terminal é insta-le a biblioteca "qrcode" >>> pip install qrcode
# insta-le também >>> pip install Image

import qrcode

link = input('Digite o link para gerar o QRCode: ')

imagem = qrcode.make(link)

imagem.save("qrcode.jpg")

print('Pronto!')