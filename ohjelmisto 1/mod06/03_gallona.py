def muunnos(gallona):
    litra = gallona * 3.785
    return litra
while True:
    gallona = int(input('syötä gallonamäärä: '))
    if gallona < 0:
        break
    else:
        print(f'{gallona} gallonaa on {muunnos(gallona)} litraa.')
print('negatiivinen gallonamäärä syötetty. ohjelma lopetettu.')