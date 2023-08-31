import random

pisteidenmaara = float(input('anna pisteiden määrä:'))
alkuperainenmaara = pisteidenmaara
pisteetympyrassa = 0

while pisteidenmaara > 0:
    pisteidenmaara = pisteidenmaara - 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        pisteetympyrassa = pisteetympyrassa + 1
piinarvo = (4 * pisteetympyrassa)/alkuperainenmaara
print(f'{alkuperainenmaara:.0f} pisteestä {pisteetympyrassa} on ympyrän sisällä. Piin arvoksi laskettu {piinarvo}')