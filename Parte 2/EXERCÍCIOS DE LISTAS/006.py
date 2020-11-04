op = 1
lista = []
i = 0
tri = 1
lista2 = []
while op == 1:
     lista.append(int(input('Digite o num a ser adicionado na lista:')))
     op = int(input('Deseja continuar? 1-sim, 2-não'))
while i<len(lista):
     tri = lista[i] *lista[i] * lista[i]
     lista2.append(tri)
     i = i+1
print('A:',lista)
print('Cubo:',lista2)
