def num(a):
     try:
       a = int(a)
       m = 1
       for i in range(a,0,-1):
           m = i * m
       return m
     except ValueError:
          return False


a = 5
print(num(a))
