VAR_GLOBAL ="Variável definida fora da função"

def imprimir_frase():
    VAR_GLOBAL = "Variável definida na função imprimir_frase()"
    print('Dentro da função - var.global:',VAR_GLOBAL)
    print('Dentro da função - var.local:',VAR_LOCAL)

#_____________________________________________________________________
imprimir_frase()
print(VAR_GLOBAL)
print(VAR_LOCAL)
