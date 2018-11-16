def get_even_list(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(*get_even_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
 