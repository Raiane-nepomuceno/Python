b = str(input('Digite a segunda string[aa/aa/aaaa]:'))
if (int(b[0:2])>31 or int(b[0:2])< 0) and (int(b[4:5])>12 or int(b[4:5])<0) or (int(b[6:10])<1900 or int(b[6:110])>2020):
       print('A data: {} está inválida.'.format(b))
        
#else:
 #   print('A data: {} está correta'.format(b))
print(int(b[0:2]))
print(int(b[4:5]))
print(int(b[6:10])) 
