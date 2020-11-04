#Crie um programa que leia
#Inicialmente uma sequencia de
#N números inteiros
#e mostre ao final 2 listas: uma sem repetição e outra dos elementos repetidos
op = 1
lista_rep = []
lista3 = []
while op == 1:
     op = int(input('Deseja adicionar o elemento [1-sim/2-não]:'))
     if op == 1:
          n = int(input('Num:'))
          if n not in lista3:
               lista3.append(n)
          elif n in lista3:
               lista_rep.append(n)
     if op == 2:
          print('Lista sem repetição:',lista3)    
          print('Lista dos elementos repetidos:',lista_rep)
     
     
     
