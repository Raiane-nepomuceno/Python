def fatorial(n):
    if n <= 1:
        return 1
    else:
        valor = n * fatorial(n-1)
        return valor
#__________________________________Programa Principal______________________________________

print(fatorial(5))
