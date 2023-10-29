luvut = []
while True:
    luku = input('anna luku: ')
    if luku != "":
        luku = float(luku)
        luvut.append(luku)
    else:
        break
luvut.sort(reverse=True)
print(luvut[:5])