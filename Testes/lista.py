def double_stuff(lista):
    for posicao in range(len(lista)):
        lista[posicao] = 2 * lista[posicao]


#___________________________________
#Programa Principal        
things = [2, 5, 9]
print(things)#antes da modificação
double_stuff(things)
print(things)#depois da modificação
