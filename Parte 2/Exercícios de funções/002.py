#Faça uma função que receba uma lista
#como parâmetro e retorne sua soma
def soma(lista):
    soma = 0
    for i in lista:
         soma = soma + i
    return soma





#------------------------------
lista = []
op = int(input('Quantos elementos deseja adicionar na lista:'))
for c in range(op):
    lista.append(int(input('Digite o elemento que deseja adicionar:')))
print(soma(lista))
    
    
