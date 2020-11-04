#Crie um programa que leia inicialmente uma sequência de N números
#inteiros e ao seu final mostre a sequência original,
#a soma de seus elementos que forem pares e a multiplicação dos elementos
#que forem impares. 
lista = []
soma = 0
mult = 1
op=1
lista_soma = []
lista_mult = []
i = 0
j = 0
#o que for par = soma , impar =*
while op ==1:
     op = int(input('Deseja adicionar um elemento [1]sim,[2]não:'))
     if op == 1:
        n = int(input('Digite o número:'))
        lista.append(n)
        if n % 2 == 0:
             lista_soma.append(n)
        else:
             lista_mult.append(n)
             
while i<len(lista_soma): 
     soma = lista_soma[i] + soma
     i = i+1
     
while j<len(lista_mult):
     mult = lista_mult[j] * mult
     j = j + 1
print('Soma dos números pares:',soma)
print('Multiplicação dos números ímpares:',mult)
print('Lista:',lista)

