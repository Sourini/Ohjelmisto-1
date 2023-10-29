import random
luku = random.randint(1,10)
arvaus = float(input('arvaa luku 1 ja 10 välillä:'))
while arvaus != luku:
    if arvaus > luku:
        print('liian suuri arvaus')
    if arvaus < luku:
        print('liian pieni arvaus')
    arvaus = float(input('anna uusi arvaus:'))
print(f'luku {luku} oli oikein!')