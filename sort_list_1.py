
def sort_list(lista):

    count = 0
    loop = 0

    while not count == len(lista)-1:

        # Verifica se todos os valores estão em ordem crescente.
        for index in range(len(lista) - 1):
            if lista[index] <= lista[index + 1]:
                count += 1

        if count == len(lista) - 1:
            break
        else:
            count = 0

        # Altera a ordem dos elementos da lista
        for index in range(len(lista)-1):
            if lista[index] > lista[index + 1]:
                lista[index], lista[index + 1] = lista[index + 1], lista[index]

        loop += 1


l1 = [2, 3, 2, 5, 72, 6, 1, 8, 1, 2, 3, 4, 5, 7, 1, 2, 1, 10, 2, 23, 0]

print(l1)
sort_list(l1)
print(l1)
