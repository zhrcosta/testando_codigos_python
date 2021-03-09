
def sort_list(lista):

    s_lista = lista
    count = 0
    loop = 0

    while not count == len(s_lista)-1:

        count = 0

        # ALtera a ordem dos elementos da lista
        for index in range(len(s_lista)-1):
            if s_lista[index] > s_lista[index+1]:
                s_lista[index], s_lista[index +
                                        1] = s_lista[index+1], s_lista[index]

        # Verifica se todos os valores estão em ordem crescente.
        for index in range(len(s_lista)-1):
            if s_lista[index] <= s_lista[index + 1]:
                count += 1

        loop += 1

    print(2*'\n')
    print(f'Repetições do laço: {loop}')
    print(f'Comprimento da lista: {len(s_lista)}')
    print(s_lista)
    print(2*'\n')

    return s_lista

l1 = [2, 3, 2, 5, 72, 6, 1, 8, 1, 2, 3, 4, 5, 7, 1, 2, 1, 10, 2, 23, 0]

sort_list(l1)
