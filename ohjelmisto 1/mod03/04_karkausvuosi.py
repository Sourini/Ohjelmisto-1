vuosi = float(input('anna vuosiluku:'))
if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
    print(f'{vuosi:.0f} on karkausvuosi!')
else:
    print(f'{vuosi:.0f} ei ole karkausvuosi!')