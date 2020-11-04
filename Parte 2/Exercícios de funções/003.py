#Faça uma função que receba 2 strings e retorne True se a segunda string é um
#anagrama da primeira, ou False caso contrário.

#EX: OVA
#VOA
def anagrama(a,b):
    ang = True
    for i in a:
        if i not in b:
            ang = False                                                                                                                                                                                                                                                                                                                                                           
    if ang:
        for i in b:
            if i not in a:
                ang = False
    return ang
        


#Programa Principal
a = str(input('Digite a primeira palavra:'))
b = str(input('Digite a segunda palavra:'))
if anagrama(a,b):
    print('É um anagrama')
else:
    print('Não é um anagrama')
