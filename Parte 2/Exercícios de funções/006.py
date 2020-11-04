#Faça uma função que calcule o fatorial de um número inteiro positivo
#(faça a consistência). Transforme seus programas de consistência de
#número já implementados (Aula 8 – exs 8 e 9) para funções.


def num(a):
     try:
       a = int(a)
       m = 1
       for i in range(a,0,-1):
           m = i * m
       return m
     except ValueError:
       return False



#Aula 8 - verificar se pode ser conferido

#--------------------PROGRAMA PRINCIPAL-----------------------------------
a = str(input('Digite o número a ser calculado a fatorial:'))
print('Fatorial é:',num(a))

   
   
   
