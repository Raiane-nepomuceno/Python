op = 1
lista = []
maior = 0
while op == 1:
     op = int(input('Deseja continuar [1]sim,[2]não:'))
     if op == 1:
          lista.append(float(input('Digite a altura:')))
          for i in lista:
               if i > maior:
                   maior = i

     else:
         print('A lista das alturas',lista)
         print('O maior número é: {} e a posição:[{}]'.format(maior,lista.index(maior)))
     
