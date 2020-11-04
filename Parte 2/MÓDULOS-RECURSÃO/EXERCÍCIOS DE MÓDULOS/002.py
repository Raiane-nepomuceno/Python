#2 listas de entrada como parametro
#união, intersecção, diferença, soma, subtração, multiplicação, divisão, e lista resultado
def info():
     a = []
     b = []
     matriz = []
     op1 = int(input('Digite a quantidade de elementos da primeira lista:'))
     op2 = int(input('Digite a quantidade de elementos da segunda lista:'))
     for c in range(op1):
          a.append(float(input('Informe o elemento a ser adicionado na lista 1:')))
     for i in range(op2):
           b.append(float(input('Informe o elemento a ser adicionado na lista 2:')))
     matriz.append(a)
     matriz.append(b)
     print('-='*30)
     print('Lista 1:',a)
     print('Lista 2:',b)
     uniao(a,b)
def uniao(a,b):
     lista_resultado = []
     matriz = []
     for i in a:
          if i not in lista_resultado:
               lista_resultado.append(i)
     for j in b:
          if j not in lista_resultado:
               lista_resultado.append(j)
     matriz.append(lista_resultado)
     print('Lista União:',lista_resultado)
     print('Matriz geral:',matriz)
     inter(a,b)
def inter(a,b):#---------------- corrigir porque esta repetindo -------
     lista_inter = []
     for i in a:
          if i in b:
             lista_inter.append(i)
     print('Lista Intersecção:',lista_inter)
     soma(a,b)
def soma(a,b):
     i = 0
     soma = 0
     d = []
     while i<len(a):
          while i<len(b):
               soma = a[i] + b[i]
               d.append(soma)
               i = i + 1
     print('A somatória das listas:',d)
     sub(a,b)
def sub(a,b):
     i = 0
     sub = 0
     d = []
     while i<len(a):
          while i<len(b):
               sub = a[i] - b[i]
               d.append(sub)
               i = i + 1
     print('A subtração das listas:',d)
     mult(a,b)
def mult(a,b):
     i = 0
     mult = 0
     d = []
     while i<len(a):
          while i<len(b):
               mult = a[i] * b[i]
               d.append(mult)
               i = i + 1
     print('A multiplicação das listas:',d)
     div(a,b)
def div(a,b):
     i = 0
     div = 0
     d = []
     while i<len(a):
          while i<len(b):
               div = a[i] / b[i]
               d.append(div)
               i = i + 1
     print('A divisão das listas:',d)
     
#_____________PROGRAMA PRINCIPAL_______________________________
info()     
     

