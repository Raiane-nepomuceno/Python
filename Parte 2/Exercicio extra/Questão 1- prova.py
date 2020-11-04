import math
def pot(lista):
     l2 = []
     for d in lista:
          r = math.pow(d,lista.index(d))
          l2.append(r)
     print('A potênciação dos elementos é:',l2)
     op = str(input('Deseja somar os elementos [S/N]:')).upper()
     if op == 'S':
          soma(l2)
     else:
          print('A lista adicionada é:',lista)
def soma(l2):
     s = 0
     for i in l2:
          s = s + i
     print('A soma da lista é:',s)

#____________________________________________________________
     
n = int(input('Digite a quantidade de elementos:'))
lista = []
for i in range(n):
     lista.append(int(input('Digite o elemento:')))
pot(lista)
