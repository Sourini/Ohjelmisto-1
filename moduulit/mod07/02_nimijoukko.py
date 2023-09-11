nimijoukko = set()

while True:
    nimi = input('syötä nimi: ')
    if nimi == "":
        break
    else:
        vanhaMitta = len(nimijoukko)
        nimijoukko.add(nimi)
        uusiMitta = len(nimijoukko)
    if vanhaMitta == uusiMitta:
        print(f'{nimi} on jo listalla!')
    else:
        print(f'{nimi} lisätty listaan!')

print('tyhjä syöte, listataan kaikki syötetyt nimet:')
for i in nimijoukko:
    print(i)