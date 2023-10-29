def listaf(lista):
    summa = 0
    for i in range(0, len(lista)):
        summa = lista[i] + summa
    return summa

lista = [1,2,3,4]
summa = listaf(lista)
print(summa)