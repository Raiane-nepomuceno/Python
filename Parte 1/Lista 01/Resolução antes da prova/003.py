#Paulo custará R$ 500,00 o metro quadrado e se estiver em
#Curitiba custará R$ 450,00 o metro quadrado. 
 
 
l = float(input('Digite o lado do terreno:'))
c = float(input('Digite o comprimento do terreno:'))
m = l*c
op = int(input('Este lote está localizado[ 1-SP,2-Curitiba]:'))
if op == 1:
   print(500*m)
if op == 2:
     print(450*m)
               
