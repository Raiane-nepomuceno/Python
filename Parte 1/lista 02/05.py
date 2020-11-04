n = 1
maior = 0
menor = 9999999
contador = 0 #contador de alunos
while n > 0:
    n = float(input('Nota:'))
    if n > 0:
        contador = contador + 1
        if n > maior:
            maior = n
        else:
            if n<menor:
                menor = n
print('Contablizamos {} notas'.format(contador))
print('Maior:',maior)
print('Menor:',menor)


        
