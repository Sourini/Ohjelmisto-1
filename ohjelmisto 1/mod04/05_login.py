username = "python"
password = "rules"
fails = 0
while fails < 5:
    user = input('käyttäjänimi:')
    pw = input('salasana:')
    if username != user or password != pw:
        print('väärin. syötä uudet käyttäjätunnukset')
    if username == user and password == pw:
        break
if fails >= 5:
    print('käyttäjätunnukset syötetty väärin liian monta kertaa')
else:
    print('tervetuloa')