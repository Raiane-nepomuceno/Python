op = 1
lista =[]
lista2 = []
while op == 1:
     lista.append(int(input('Num que será adicionado na lista:')))
     op = int(input('1-continuar,2 -sair'))
print(lista[::-1])
