op = 1
i = 0
lista1 = []
lista2 = []
lista3 = []
soma = 0
while op == 1:
      lista1.append(int(input('Informe o num a ser adicionado na lista 1:')))
      lista2.append(int(input('Informe o num a ser adicionado na lista 2:')))
      op = int(input('Deseja continuar, se sim digite 1 senão digite 2:'))
while i < len(lista1):
     while i<len(lista2):
          soma = lista1[i] + lista2[i]
          lista3.append(soma)
          i = i + 1
print('A:',lista1)
print('B:',lista2)
print('Soma:',lista3)
     
