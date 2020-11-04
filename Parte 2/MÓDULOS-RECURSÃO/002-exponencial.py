def potencia(x,y):
     if y == 0:
          return 1
     else:
          return x * potencia(x,y-1)

#______________________________________

x = int(input('Digite a base:'))
y = int(input('Digite o expoente:'))
print('Resultado:',potencia(x,y))



