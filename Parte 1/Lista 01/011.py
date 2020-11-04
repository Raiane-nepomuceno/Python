n= int(input('Digite o número:'))
if n%2== 0 and n%5 == 0 and n%10 == 0:
    print('O número {} é divisível por:2,5,10'.format(n))
elif n%2!= 0 and n%5 == 0 and n%10 == 0:
    print('O número {} é divisível por 5 e 10'.format(n))
elif n%2!= 0 and n%5 == 0 and n%10 != 0:
    print('O número {} é divisível apenas por 5'.format(n))
elif n%2== 0 and n%5 != 0 and n%10 != 0:
    print('O número {} é divisível apenas por 2'.format(n))
else:
    print('Nenhum dos números são divisíveis')
