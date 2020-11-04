pi = 0
a = int(input('Num:'))
i = 0 # variavel de controle
b = a - 1 #controle do expoente
while i < a:
      if i%2!=0:
        pi = pi+ (a/b)
        print('1:', pi)
      else:
          pi = (a - a/b)
          print('2:',pi)
      b = b + 2
      i = i + 1

print(pi)
