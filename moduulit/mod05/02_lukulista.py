luvut = []
luku = 0
while luku != "":
    luku = input('anna luku: ')
    if luku != "":
        luku = float(luku)
        luvut.append(luku)
luvut.sort(reverse=True)

print(luvut[:5])