lista_geral = []
lista2 = []
for i in range(4):
     lista = []
     lista.append(int(input('Num:')))
     lista_geral.append(lista)
for i in range(len(lista_geral)):
     for j in range(0,len(lista_geral)):
          if j %2 == 0:
               lista2.append(j)
print(lista2)
