op = 1
i = 0
lista = []
lista1 = []
while op ==1:
     lista.append(int(input('Digite o elemento:')))
     op=int(input('1-continuar,2-sair:'))
while i<len(lista):
     if lista[i] % 2 == 0:
          lista1.append(1)
          i = i + 1
     else:
          lista1.append(-1)
          i = i+1
print('lista A:',lista)
print('Lista final:',lista1)
          
