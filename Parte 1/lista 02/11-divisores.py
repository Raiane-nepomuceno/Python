n = int(input('Valor:'))
div = 1 #para contabilizar o divisor

i = 1 #inicializar com o 1 e controlar a estrutura de repetição

while i < n:
    if n % i == 0:
        div = div + 1
        i = i+1
    else:
        i = i + 1


print(div)
