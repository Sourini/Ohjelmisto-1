lentoasemat = {}

while True:
    valikko = input('haluatko syöttää uuden lentoaseman (1), hakea jo syötetyn lentoaseman tiedot (2) vai lopettaa (3)? ')
    if valikko == "3":
        break
    elif valikko == "2":
        icaoHaku = input('syötä haettavan lentoaseman ICAO-koodi: ')
        if icaoHaku in lentoasemat:
            print(lentoasemat[icaoHaku])
        else:
            print('virheellinen syöte, paltaan alkuun')
    elif valikko == "1":
        icao = input('syötä uuden lentoaseman ICAO-koodi: ')
        lentoasema = input(f'syötä lentoaseman {icao} nimi: ')
        lentoasemat[icao] = lentoasema
    else:
        print('virheellinen syöte, palataan alkuun.')
print('ohjelman käyttö lopetettu.')