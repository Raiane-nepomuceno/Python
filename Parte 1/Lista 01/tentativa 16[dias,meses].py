d = int(input('Digite a data:'))
m = int(input('Digite o mês [1-Janeiro/2-Fevereiro]:'))
        #quantidade de dias para o final de ano.Todos os meses tem 30 dias
ano=12*30 #total de dias de um ano
mes = 30 
t=(mes*m)-(d-ano) #total de dias em meses passados #desconto do dia no total do ano
print(t)
      
