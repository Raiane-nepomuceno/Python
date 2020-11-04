#Quantos são maiores que 10
cont = 0
for i in range(0,5):
    valor = float(input('Digite o número:'))
    if valor > 10:
        cont = cont + 1
print('Há {} números maiores que 10'.format(cont))
     
        
