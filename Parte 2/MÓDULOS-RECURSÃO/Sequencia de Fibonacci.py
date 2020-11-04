def sequencia_fibonacci(a,b,n):
    if a < n:
        print(a," ", end = "")
    if b < n:
        sequencia_fibonacci(b, a + b,n)

nro=5
sequencia_fibonacci(0,1,nro)
    
