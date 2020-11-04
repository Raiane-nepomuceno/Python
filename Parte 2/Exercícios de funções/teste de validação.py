def num(s):
     try:
       return int(s)
     except ValueError:
       return False

s = str(input('Num:'))
print(num(s))
