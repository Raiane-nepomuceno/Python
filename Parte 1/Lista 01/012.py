print('-='*30)
print('Analisando se forma triângulos')
print('-='*30)
a =float(input('Primeiro segmento:'))
b =float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))

if a < b+c and b < a+c and c < b+a:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if a==b ==c:
        print('Tipo:Equilátero')
    elif a == b and b!=c:
        print('Tipo:Isósceles')
    elif c == a and c!=b:
        print('Tipo:Isósceles')
    elif c == b and b!=a:
        print('Tipo:Isósceles')
    elif  a!=b and b!=c:
        print('Tipo:Escaleno')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

