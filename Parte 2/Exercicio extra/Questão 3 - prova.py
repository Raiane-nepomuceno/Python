def cont_caractere(palavra):
     dic = {}
     for i in palavra:
         r = palavra.count(i)
         dic[i] = r
     print(dic)
     
palavra = str(input('Digite o texto:'))
cont_caractere(palavra)
