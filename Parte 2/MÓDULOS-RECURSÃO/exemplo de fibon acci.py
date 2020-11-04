def termo_fibonacci(n):
    if n <= 1:
        return n
    else:
        return termo_fibonacci(n-1) + termo_fibonacci(n-2)



nro = 5
if nro < 0:
    print('O número deve ser maior ou igual a zero')
else:
    print(termo_fibonacci(nro))
    
