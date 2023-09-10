def listaf(lista):
    for i in range(1, len(lista)):
        if i % 2 == 0:
            parilista.append(i)
    return parilista

lista = [1,2,3,4,5,6,7,8,9]
parilista =[]

print(lista)
print(listaf(lista))
