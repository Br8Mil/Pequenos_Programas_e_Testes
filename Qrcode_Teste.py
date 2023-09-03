import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=30,
    border=2
)

qr.add_data('#link aqui')

qr.make(fit=True)

imagem = qr.make_image(fill_color='black', back_color='white')

imagem.save('qrcode.png')