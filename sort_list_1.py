
def sort_list(lista):

    s_lista = lista
    count = 0
    loop = 0

    while not count == len(s_lista)-1:

        # Verifica se todos os valores estão em ordem crescente.
        for index in range(len(s_lista)- 1 ):
            if s_lista[index] <= s_lista[index + 1]:
                count += 1
            
        if count == len(s_lista) - 1:
            return s_lista, loop
            break
        else:
            count = 0

        # Altera a ordem dos elementos da lista
        for index in range(len(s_lista)-1):
            if s_lista[index] > s_lista[index + 1]:
                s_lista[index], s_lista[index + 1] = s_lista[index + 1], s_lista[index]


        loop += 1

    return s_lista, loop

l1 = [2, 3, 2, 5, 72, 6, 1, 8, 1, 2, 3, 4, 5, 7, 1, 2, 1, 10, 2, 23, 0]


print(sort_list(l1))
