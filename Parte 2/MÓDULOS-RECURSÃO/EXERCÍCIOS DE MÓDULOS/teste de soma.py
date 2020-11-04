a = [10,8,7,6,2]
b = [5,4,3,2,1]
i = 0
soma = 0
d = []
while i<len(a):
     while i<len(b):
          soma = a[i] - b[i] 
          d.append(soma)
          i = i + 1
print(a)
print(b)
print(d)
