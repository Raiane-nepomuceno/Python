import ValidaValores


x=input("Digite um número INTEIRO POSITIVO:")
while not ValidaValores.ValidaInteiroPositivo(x):
    print(x, "não é um número inteiro positivo!")
    x=input("Digite um número INTEIRO POSITIVO:")
    
x=int(x)
print("O valor do inteiro positivo convertido por int() é:", x, "\n")


x=input("Digite um número INTEIRO:")
while not ValidaValores.ValidaInteiro(x):
    print(x, "não é um número inteiro!")
    x=input("Digite um número INTEIRO:")
    
x=int(x)
print("O valor do inteiro convertido por int() é:", x,"\n")


x=input("Digite um número REAL:")
while not ValidaValores.ValidaReal(x):
    print(x, "não é um número real!")
    x=input("Digite um número REAL:")
    
x=float(x)
print("O valor convertido por float() é:", x, "\n")

    
