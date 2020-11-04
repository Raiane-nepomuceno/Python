def sum(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + sum(lista[1:])
print(sum([1,3,5,7,9]))
