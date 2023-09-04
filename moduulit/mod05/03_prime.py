luku = int(input('anna kokonaisluku: '))
prime = 0
if luku >= 3:
    for i in range(2, luku):
        if luku % i != 0:
            prime = 2
        elif luku % i == 0:
            prime = 1
            break
if prime == 0 and luku !=2:
    print(f'luvut 1 ja sitä vähemmät eivät ole alkulukuja.')
elif prime == 2 or luku == 2:
    print(f'{luku} on alkuluku.')
elif prime == 1:
    print(f'{luku} ei ole alkuluku.')