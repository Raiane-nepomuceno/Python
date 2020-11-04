def dobra_lista(lista):
    nova_lista = []
    for valor in lista:
        novo_elemento = 2 * valor
        nova_lista.append(novo_elemento)
    return nova_lista

#----------------------------------------------------------------
numeros = [3, 6, 10]
numeros_emdobro = dobra_lista(numeros)
print(numeros)
print(numeros_emdobro)
