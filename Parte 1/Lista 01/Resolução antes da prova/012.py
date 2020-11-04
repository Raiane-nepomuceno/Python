a =float(input('Primeiro segmento:'))
b =float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))
if a < b+c and b < a+c and c < b+a:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if a ==b==c:
         print('Equilátero')
    elif a==b and b!=c:
         print('Isósceles')
    elif c == a and c!=b:
         print('Isósceles')
    elif c == b and b!=a:
          print('Isósceles')
    elif a!=b and b!=c:
         print('Escaleno')
else:
     print('não podem formar um triângulo')

         
