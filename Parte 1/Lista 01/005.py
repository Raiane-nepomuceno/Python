#de Massa Corporal é: IMC = peso / (altura)2
#Faça um programa que calcule o IMC de uma pessoa.
#A partir do IMC, A Organização Mundial de Saúde usa um critério simples: Condição IMC em adultos
#abaixo do peso abaixo de 18,5
#peso normal entre 18,5 e 25
#acima do peso entre 25 e 30
#obeso acima de 30
p = float(input('Digite o peso:'))
a = float(input('Digite a altura:'))

imc = p/(a*a)

if  imc <18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <25:
    print('Peso normal')
elif imc>= 25 and imc <30:
    print('Acima do peso')
else:
    print('Obeso')
