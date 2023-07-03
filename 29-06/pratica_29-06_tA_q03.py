#Prova prática dia 29/06 tipo A (Questão 03)
def mediaAritmetica(listaNumeros):
    soma = 0
    for i in listaNumeros:
        soma += i

    return soma/len(listaNumeros)

#Main
q = int(input("Qts? "))
numeros = []
for i in range(q):
    numeros.append(int(input("Number: ")))

print(mediaAritmetica(numeros))
