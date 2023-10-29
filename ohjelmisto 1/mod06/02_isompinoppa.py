import random


def heitto(sivut):
    noppa = random.randint(1, sivut)
    return noppa


sivut = int(input('anna nopan sivujen määrä: '))
throw = heitto(sivut)

while throw != sivut:
    print(throw)
    throw = heitto(sivut)
print(throw)
