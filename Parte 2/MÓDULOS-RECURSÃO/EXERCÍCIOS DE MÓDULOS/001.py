import ValidaValores

x=str(input('num:'))

if ValidaValores.ValidaInteiroPositivo(x):
     print("O Número digitado é um Inteiro Positivo!")
elif ValidaValores.ValidaInteiro(x):
     print("O Número digitado é um Inteiro!")
elif ValidaValores.ValidaReal(x):
     print('O número digitdo é Real')
 
