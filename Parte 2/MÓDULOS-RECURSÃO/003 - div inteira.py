#quociente
def div(x,y):#a = 8 b = 4 
     if  x == y:
          return 1 
     else:
          return  div(x,y+1)
x = int(input('Digite o dividendo:'))
y = int(input('Digite o divisor:'))
print('Quociente:',div(x,y))
