import random
heittomaara = 0
kuutiot = int(input('anna arpakuutioiden määrä: '))
for heitot in range(kuutiot):
    heittomaara = heittomaara + 1
    print(f'heitto numero {heittomaara}: {random.randint(1,6)}!')