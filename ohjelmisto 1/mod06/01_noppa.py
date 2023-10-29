import random


def heitto():
    noppa = random.randint(1, 6)
    return noppa


throw = heitto()
while throw != 6:
    print(throw)
    throw = heitto()
print(throw)
