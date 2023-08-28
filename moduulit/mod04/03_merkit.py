luku = input('anna luku:')
pienin = luku
suurin = luku
while suurin >= pienin:
    luku = input('anna uusi luku:')
    if luku == "":
        break
    if luku < pienin:
        pienin = luku
    if luku > suurin:
        suurin = luku

print(f'suurin antamasi luku oli {suurin} ja pienin oli {pienin}')