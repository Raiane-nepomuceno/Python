#5 num e diz qual é o maior
contador = 0
maior = 0
while contador < 5:
    n = float(input('Num:'))
    if n > maior:
        maior = n
    contador = contador + 1
print('O maior número é:',maior)
