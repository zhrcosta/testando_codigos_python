
def sort_list(lista):

    s_list = lista

    count = 0

    if len(lista) == 1:
        return s_list

    elif len(lista) == 2:
        if s_list[0] == s_list[1]:
            return s_list

        elif s_list[0] > s_list[1]:
            s_list[0], s_list[1] = s_list[1], s_list[0]
            return s_list

    elif len(lista) == 3:

        min = s_list[0]
        max = s_list[0]

        for num in s_list:

            if num < min:
                min = num

            if num > max:
                max = num

            s_list[0], s_list[-1] = min, max

        return lista

    while not count == len(lista)-1:

        count = 0


l = [2, 1]

print(sort_list(l))
