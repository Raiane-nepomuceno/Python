n = int(input('Digite a idade do possível eleitor:'))
if n < 16:
    print('Abaixo de 16 anos')
elif n >= 18 and n <= 65:
    print('Eleitor obrigatório')
elif n>=16 and n < 18 or n > 65:
    print('Eleitor facultativo')
