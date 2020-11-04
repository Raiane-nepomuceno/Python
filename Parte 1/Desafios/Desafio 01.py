#Como fazer para contar a quantidade de números pares entre dois numeros quaisquer?
n1 = int(input('Valor:'))
n2 = int(input('Valor:'))
cont = 0
while n1 <= n2:
      if n1 %2 == 0:
          cont = cont + 1
      n1 = n1+1
print(cont)
