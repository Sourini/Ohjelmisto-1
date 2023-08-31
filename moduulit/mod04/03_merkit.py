luku = input('anna luku:')
pienin = float(luku)
suurin = float(luku)
while suurin >= pienin:
    luku = input('anna uusi luku:')
    if luku == "":
        break
    if float(luku) < pienin:
        luku = float(luku)
        pienin = luku
    if float(luku) > suurin:
        luku = float(luku)
        suurin = luku

print(f'suurin antamasi luku oli {suurin} ja pienin oli {pienin}')