#Prova prática dia 27/06 tipo B (Questão 03)
def maiorImpar(listaNumeros):
    maior = -1
    for i in listaNumeros:
        if i % 2 == 1 and i > maior:
            maior = i

    return maior

#Main
t = int(input("Qts números? "))
numeros = []
for i in range(t):
    numeros.append( int(input("Número: ")) )

print(maiorImpar(numeros))
