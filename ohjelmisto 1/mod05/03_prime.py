luku = int(input('anna kokonaisluku: '))
prime = False
if luku >= 3:
    for i in range(2, luku):
        if luku % i != 0:
            prime = True
        elif luku % i == 0:
            prime = False
            break
if prime is True or luku == 2:
    print(f'{luku} on alkuluku.')
elif prime is False:
    print(f'{luku} ei ole alkuluku.')