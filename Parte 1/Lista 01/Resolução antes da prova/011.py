n = int(input('Escreva um valor:'))
if n % 2!=0 and n%5!=0 and n%10!=0:
     print('Não é divisível pelos números 2,5,10')
elif n%2 == 0 and n % 5 == 0 and n % 10 == 0:
     print('São divisíveis por 2,5,10')
elif n%2 == 0 and n % 5 !=0  and n % 10 != 0:
     print('É divisível por 2')
elif n%2 != 0 and n % 5 == 0 and n % 10 != 0:
     print('É divisível por 5')

