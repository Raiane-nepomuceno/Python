temperatura = []#lista da temperatura
media = 0
count = 0 #contador 
dias = 7 #total de dias
for i in range(dias):
    temperatura.append(float(input('Temperatura:')))
    media = media + temperatura[i]#somando a media mais o indice de cada elemento da lista
media = media/7

for i in range(dias):
    if (temperatura[i]>media):#se a temperatura do indice for maior que a media 
        count+=1#soma +1
print('Dias da semana acima da média',count)
