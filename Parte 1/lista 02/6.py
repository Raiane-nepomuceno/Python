contador = 0
cont2 = 0
cont3 = 0
nota = 0
while nota >=0:
    print('OBS:PARA FINALIZAR DIGITE -1:')
    nota = float(input('Nota do aluno:'))
    if nota >=6:
        contador = contador + 1
    elif nota >= 4 and nota < 6:
        cont2 = cont2 + 1
    elif nota > 0 and nota < 4 :
        cont3 = cont3 + 1
        
print('Fim do programa')
print('Há {} notas maiores que 6'.format(contador)) 
print('Há {} notas maiores que 4 e menores que 6'.format(cont2))
print('Há {} notas menores que 4.'.format(cont3))
        
                    
