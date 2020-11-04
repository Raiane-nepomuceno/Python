#i = 10
#num = 100
#cont = 0
#soma = 0
def soma(num,i):
     cont = 0
     s =0
     if soma<=num:
          return soma(num(s+i))
     else:
          return cont+1
#while soma<=num:
   #  soma = soma + i
    # cont = cont+1
#print(cont-1)
    
num = int(input('Digite a base:'))
i = int(input('Digite o expoente:'))
print('Resultado:',soma(num,i))
