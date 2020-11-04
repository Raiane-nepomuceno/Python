lista1 = []
lista2 = []
lista_uni = []
lista_mult = []
maior = 0
maior2 = 0
soma_lista1 = 0
prox = 0
ant = 0
lista = []
print('-='*30)
print(' - Menu das ações:')
print('-='*30)
print('''[1]inserir elemento na lista 1
[2]Inserir elementos na lista 2
[3]Exibir o conteúdo das duas listas
[4]Exibir a lista união da lista 1 e lista 2
[5]Exiber intersecção da lista 1 e lista 2
[6]Exibir os maiores valores da lista 1 e lista 2
[7]Multiplicar os elementos 
[8]Zerar o conteúdo das duas listas)
[9]Lista União em ordem crescente''')
print('-='*30)
op = 1

while op > 0:
    op = int(input('O que deseja fazer:'))
    if op == 1:
        for c in range(5):
            n = float(input('O que deseja inserir na lista 1:'))
            if c == 0 or n > lista1[-1]:#se for o 1 valor vai adicionar, se o num for maior que o ultimo elemento 
              lista1.append(n)
            else :
                pos = 0
                while pos < len(lista1):
                   if n <= lista1[pos]:# se o num é maior
                        lista1.insert(pos,n)
                        break
                   pos = pos + 1
        print('-='*30)
        print('Lista 1:',lista1)
        print('-='*30)

    elif op == 2:
            n = float(input('O que deseja inserir na lista 2:'))
            lista2.append(n)
            lista2.append(lista2[0]*2)
            lista2.append(lista2[1]*2)
            lista2.append(lista2[2]*2)
            lista2.append(lista2[3]*2)
            print('-='*30)
            print('Lista 2:',lista2)
            print('-='*30)

    elif op == 3:
        print('-='*30)
        print('Lista 1:',lista1)
        print('Lista 2:',lista2)
        print('-='*30)
              
    elif op == 4:
        for i in lista1:
            if i not in lista_uni:
                lista_uni.append(i)
                for i in lista2:
                    if i not in lista_uni:
                        lista_uni.append(i)
                        
        print('Lista União:',lista_uni)
        print('-='*30)
    elif op == 5:
        for i in lista1:
            if i in lista2:
                lista_uni.append(i)
        print('-='*30)
        print('Lista Intersecção:',lista_uni)
        print('-='*30)
    elif op == 6: 
         for i in lista1:
              if i > maior:
                maior = i
         for i in lista2:
                if i > maior2:
                    maior2 = i
         for elemento in lista1:
                soma_lista1+= elemento
         print('-='*30)
         print('Maior da lista 1:',maior)
         print('Maior da lista 2:',maior2)
         print('Soma dos maiores aos itens da lista 1:',soma_lista1+maior2+maior)
         print('-='*30)

    elif op == 7:#perguntar como seria com o for
        lista_mult.append(lista1[0]*lista2[0])
        lista_mult.append(lista1[1]*lista2[1])
        lista_mult.append(lista1[2]*lista2[2])
        lista_mult.append(lista1[3]*lista2[3])
        lista_mult.append(lista1[4]*lista2[4])
        print('Lista dos elementos multiplicados',lista_mult)
    elif op == 8:
        del(lista1[0:(len(lista1))])
        del(lista2[0:(len(lista2))])
        print('Lista 1 e Lista 2 foram zeradas com sucesso.')
    elif op == 9:
        for j in range(4):
            for i in range(4):
                if lista1[i]<lista1[i+1]:
                    aux = lista1[i]
                    lista1[i] = lista1[i+1]
                    lista1[i+1] = aux
        print('Lista 1:',lista1)
    elif op > 9 or op < 0:
      print('Opção inválida.Tente novamente.')
        
        
    

         
