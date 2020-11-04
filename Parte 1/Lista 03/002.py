prox = 0
count = 0
total = 9
vetor =[]
for i in range(total):
    vetor.append(int(input('Digite o valor:')))
for i in range(total):
    for x in range(total):
        ant = vetor[i]
        prox = vetor[x]
    if ant!=prox:
        count+=1

print(count)
